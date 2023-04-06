from imu import IMU
from file_io import *
import pandas as pd
class RkkGlove:
    
    DATA_HEAD = ['acc_x_1','acc_y_1','acc_z_1','rot_x_1','rot_y_1','rot_z_1',
                    'acc_x_2','acc_y_2','acc_z_2','rot_x_2','rot_y_2','rot_z_2',
                    'acc_x_3','acc_y_3','acc_z_3','rot_x_3','rot_y_3','rot_z_3',
                    'acc_x_4','acc_y_4','acc_z_4','rot_x_4','rot_y_4','rot_z_4',
                    'acc_x_5','acc_y_5','acc_z_5','rot_x_5','rot_y_5','rot_z_5',
                    'acc_x_6','acc_y_6','acc_z_6','rot_x_6','rot_y_6','rot_z_6']
    
    
    '''
    This is the class for Rkk glove, which contains 6 IMU and 1 Megenatic sensor
    '''
    __LOAD_LEN = 456
    __data_chunk_size = 60
    __first = 36
        
    '''
    isValid used to show whether there is zero reading in any imu of glove
    '''
    isValid = True
    
    imu = [IMU() for i in range(6)]
    
    def __init__(self) -> None:
        pass
    
    def loadData(self, load):
        load = bytes(load).hex()
        load_arr = []
        for i in range(len(load) // 2):
            first_char = load[2*i]
            second_char = load[2*i + 1]
            load_arr.append(first_char + second_char)
        
        if len(load_arr) != self.__LOAD_LEN:
            print('IMU CLASS: Load did not match in length:')
            print('    Expect length is: ' + str(self.__LOAD_LEN))
            print('    Actual length is: ' + str(len(load_arr)))
            return
        
        self.isvalid = True
        for i in range(6):
            start_index = self.__first + i * self.__data_chunk_size
            end_index = start_index + self.__data_chunk_size
            self.isValid = self.imu[i].setImuData(load_arr[start_index:end_index], i)
        
        
    def writePandas(self, dataFrame:pd.DataFrame):
        if dataFrame.head != self.DATA_HEAD:
            dataFrame.head = self.DATA_HEAD
        
        data = []
        for imu in self.imu:
            data += imu.getDataInDecimal()
        dataFrame.loc[len(dataFrame.index)] = data
        