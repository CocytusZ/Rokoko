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


DATA_FOLDER = './csv/20hz'




'''
Data and model import
# '''
data = [ '' for i in range(4)]
data[0] = pd.read_csv(DATA_FOLDER + '/data_0.csv')
data[1] = pd.read_csv(DATA_FOLDER + '/data_1.csv')
data[2] = pd.read_csv(DATA_FOLDER + '/data_2.csv')
data[3] = pd.read_csv(DATA_FOLDER + '/data_3.csv')
INPUT_DIM = len(data[0].columns)

model = rnn.NetModel(input_size=INPUT_DIM, hidden_size=36)
model.load_state_dict(torch.load('./model/lstm.pt'))


'''
Testing
'''

result = [[0,0] for _ in range(LABEL_NUM)]
x_test = []
y_test = []

for i in range(len(data)):
    for _ in range(TEST_SAMPLE_NUM):
        start_index = np.random.randint(len(data[i]) - SEQUENCE_NUM - 1, size=1)[0]
        df_vector = data[i].iloc[start_index : start_index + SEQUENCE_NUM]
        df_vector = np.array(df_vector).reshape(1, SEQUENCE_NUM, INPUT_DIM)
        x_test.append(df_vector)
        y_test.append(LABEL[i])
    
x_test = torch.tensor(np.array(x_test)).reshape(-1, SEQUENCE_NUM, INPUT_DIM).float()
y_test = torch.tensor(y_test).reshape(-1, LABEL_NUM).long()

y_test_pred = model(x_test)
# print(y_test_pred)
# print('Shape of x', end='')
# print( x_test.shape)
# print('Shape of y', end='')
# print( y_test_pred.shape)

for i in range(len(y_test_pred)):    
    # print('\nActual: ', end='')
    # print(y_test_pred[i], end='')
    # print('Expected: ', end='')
    # print(y_test[i])
    expected = np.argmax(y_test[i].tolist())
    actual   = np.argmax(y_test_pred[i].tolist())
    # print('Expected: {}    ====   Actual: {}'.format( expected, actual))
    if actual != expected:
        result[expected][0] = result[expected][0] + 1
    else:
        result[expected][1] = result[expected][1] + 1
    
for i in range(len(result)):
    acc_rate = result[i][1] / (result[i][1] + result[i][0])
    print('The accuracy of gesture {} is {}%'.format(i, acc_rate * 100))

