from macpath import split
from pickle import FALSE
from this import d
from file_io import *
import pandas as pd
from glove import RkkGlove

def getStatistics(csv_path):
    '''
    Get statistics feature from data
    '''
    dataFrame = pd.read_csv(csv_path)

    spliter = []
    mean_val = []
    std_val = []

    # for head in dataFrame.columns:
    #     spliter.append('------')
    #     mean_val.append(dataFrame[head].mean())
    #     std_val.append(dataFrame[head].std())

    # csvAppend(csv_path, spliter)
    # csvAppend(csv_path, mean_val)
    # csvAppend(csv_path, std_val)
    
def markOneHot(df:pd.DataFrame, mark:str, num:int):
        """
        @description  : 
            function to mark data column in one-hot encoding
        
        ---------
        @param  : 
            1. df   -> data frame need to be marked
            2. mark -> big character, which is the label of data
            3. Char -> the length of one-hot dict
        -------
        @Returns  :
        -------
        """
        
        for i in range(num):
            if i == int(mark):
                df.insert(len(df.columns), i, 1, False)
            else:
                df.insert(len(df.columns), i, 0, False)
                    

def appendAccNormCol(df:pd.DataFrame):
    '''
    Append colomuns contains the norm of accelerometer to original one
    '''
    imu_num = len(df.columns) // 3
    for i in range(imu_num):
        acc_x = df[RkkGlove.DATA_HEAD[i*3 + 0]] 
        acc_y = df[RkkGlove.DATA_HEAD[i*3 + 1]]
        acc_z = df[RkkGlove.DATA_HEAD[i*3 + 2]]
        
        acc_norm = acc_x **2 + acc_y **2 + acc_z **2 
        acc_norm = acc_norm / 10000
        df.insert(len(df.columns), 'acc_norm_' + str(i), acc_norm, FALSE)

def selectAccNorm(df:pd.DataFrame):
    '''
    return a dafaframe which only contain the norm data of accelerometer
    Do no change on the original dataframe
    '''
    new_df = pd.DataFrame()
    imu_num = len(df.columns) // 3
    for i in range(imu_num):
        acc_x = df[RkkGlove.DATA_HEAD[i*3 + 0]] 
        acc_y = df[RkkGlove.DATA_HEAD[i*3 + 1]]
        acc_z = df[RkkGlove.DATA_HEAD[i*3 + 2]]
        
        acc_norm = acc_x **2 + acc_y **2 + acc_z **2 
        acc_norm = acc_norm / 10000
        new_df.insert(len(df.columns), 'acc_norm_' + str(i), acc_norm, FALSE)
    

if __name__ == '__main__':
    print("Data_analysis.py:")
    
    csv_path = "./csv/data_test.csv"
    dataFrame = pd.read_csv(csv_path)
    appendAccNormCol(dataFrame)
    print(dataFrame)
