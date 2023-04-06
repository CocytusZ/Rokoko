from itertools import count
from pyexpat import model
from statistics import mode
from time import sleep
from pandas import DataFrame
from scapy.all import *
from glove import RkkGlove
from data_analyze import *
import rnn as rnn
import torch
import numpy as np
from data_analyze import appendAccNormCol

import tkinter as tk
'''

'''

# --------------------- Global Config ------------------------#
DATA_INTERVAL = 0.02
SEQUENCE_NUM = rnn.SEQUENCE_NUM
INPUT_DIM = 24


'''
Section for script

'''

glove = RkkGlove()      # RKK_glove

# Data frame and its counter
df = DataFrame(columns=RkkGlove.DATA_HEAD)
df_count = 0


cmd = ''                # command use to interact with thread

sniff_filter = "src 192.168.2.119 and udp"


'''
Neural network
'''
rnnModel = rnn.NetModel(input_size=INPUT_DIM, hidden_size=36)
rnnModel.load_state_dict(torch.load('./model/lstm.pt'))

predict_result = [0, 0, 0]
'''
Section of ui
'''
UI_LABEL = ['Idle', 'Scissors', 'Knife', 'Hammer']

ui = tk.Tk()
ui_label = tk.Label(ui, text='NONE')
ui_label.grid(row=0, column=0)
ui_label.config(font=("Courier", 64))
ui_label.pack()
# --------------------- method def start ------------------------#

def sniff_thread_func():
    while True:        
        print('.', end='')
        sleep(DATA_INTERVAL)        
        sniff(count=1, filter=sniff_filter, prn=callback)




def callback(packet):
    global glove
    global df
    global df_count
    
    print('.', end='')
    glove.loadData(packet.load)

    df_count = df_count + 1
    glove.writePandas(df)
    
    if(df_count >= SEQUENCE_NUM):
        df_count = 0
        rnnPredict(df)
        df.drop(df.index, inplace=True)
        
        for i in range(6):
            head = 'acc_norm_' + str(i)
            df.drop(labels=head, axis=1, inplace=True)

    # print(glove.imu[1].getDataInDecimal()[0])
    

def rnnPredict(df:DataFrame):
    global ui_label
    global predict_result
    appendAccNormCol(df)
    df = df.apply(pd.to_numeric, errors='coerce')
    data_slot = df.iloc[0:SEQUENCE_NUM]
    x_test = torch.tensor(np.array(data_slot)).reshape(1, SEQUENCE_NUM, INPUT_DIM).float()
    y_pred = rnnModel(x_test)
    
    result = np.argmax(y_pred.detach().numpy())
    predict_result.pop(0)
    predict_result.append(result)
    print(predict_result)
    
    isSame = True
    for i in range(len(predict_result) - 1):
        if predict_result[i] != predict_result[i+1]:
            isSame = False
    if isSame:
        ui_label.config(text=UI_LABEL[result])
    else:
        ui_label.config(text='.....')




# --------------------- method def end ------------------------#

save_path = ''
thread = threading.Thread(target=sniff_thread_func, args=())
thread.start()
tk.mainloop()
thread.join()
print("=============== Live Test End ===============")
