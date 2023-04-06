import numpy as np
import pandas as pd
import torch

import rnn as rnn
# from rnn import NET

'''
Config
'''
LABEL = rnn.LABEL
LABEL_NUM = len(LABEL)

TRANING_SAMPLE_NUM  = rnn.TRANING_SAMPLE_NUM
TEST_SAMPLE_NUM     = rnn.TEST_SAMPLE_NUM

BATCH_SIZE = TRANING_SAMPLE_NUM * LABEL_NUM
SEQUENCE_NUM = rnn.SEQUENCE_NUM
INPUT_DIM = rnn.INPUT_DIM


DATA_SRC = './csv/data_test.csv'


'''
Data and model import
# '''
data = pd.read_csv(DATA_SRC)
INPUT_DIM = len(data.columns)

model = rnn.NetModel(input_size=INPUT_DIM, hidden_size=36)
model.load_state_dict(torch.load('./model/lstm.pt'))


'''
Testing
'''

result = 0
x_test = []
y_test = []

for i in range(len(data) // SEQUENCE_NUM):
    start_index = i*SEQUENCE_NUM
    end_index = (i+1)*SEQUENCE_NUM
    df_vector = data.iloc[ start_index: end_index]
    df_vector = np.array(df_vector).reshape(1, SEQUENCE_NUM, INPUT_DIM)
    x_test.append(df_vector)
    
x_test = torch.tensor(np.array(x_test)).reshape(-1, SEQUENCE_NUM, INPUT_DIM).float()

y_test_pred = model(x_test)
# print(y_test_pred)
# print('Shape of x', end='')
# print( x_test.shape)
# print('Shape of y', end='')
# print( y_test_pred.shape)


expected = int(input('The expected gesture is NO.:  '))

for i in range(len(y_test_pred)):
    print(y_test_pred[i])    
        
    actual = np.argmax(y_test_pred[i].detach().numpy())
    if actual == expected:
        result = result + 1

    
print('Accuracy is {}%'.format(result / len(y_test_pred) * 100))

