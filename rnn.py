import torch
import torch.nn as nn

'''
Config
'''
NONE    =   [1, 0, 0, 0]
SCISSOR =   [0, 1, 0, 0]
KNIFE   =   [0, 0, 1, 0]
HAMMER  =   [0, 0, 0, 1]

LABEL = [NONE, SCISSOR, KNIFE, HAMMER]
LABEL_NUM = len(LABEL)

# Data size
TRANING_SAMPLE_NUM  = 50
TEST_SAMPLE_NUM     = 500

# Data size
BATCH_SIZE = TRANING_SAMPLE_NUM * LABEL_NUM
SEQUENCE_NUM = 40

'''
Model define
'''

LSTM_LAYER = 2

class NetModel(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        
        self.input_size = input_size
        self.hidden_size = hidden_size
        
        self.lstm = nn.LSTM(input_size, hidden_size, LSTM_LAYER, batch_first=True)
        self.output = nn.Linear(hidden_size, LABEL_NUM)
        self.softmax = nn.Softmax(dim=1)
        
    def forward(self, x):
        out, h = self.lstm(x)
        # print('Shape of lstm Result {}'.format(out[:,-1,:]))
        out = self.output(out[:,-1,:])
        return out
