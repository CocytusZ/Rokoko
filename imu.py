from ast import Index
from numpy import byte
from pylab import *
from requests import head 

class IMU:
    __data_chunk_size = 60
    __data_size = 4
    
    ID     =  0 
    ACC_X  =  1  
    ACC_Y  =  2
    ACC_Z  =  3
    ROT_X  =  4
    ROT_Y  =  5
    ROT_Z  =  6
    MAG_X  =  7
    MAG_Y  =  8
    MAG_Z  =  9
    TEMP   =  10
    IS_MAG =  11
    
    data = []
    
    def __init__(self):   
        self.data = ["00000000" for i in range(self.__data_chunk_size // self.__data_size)]
    
    
    def setImuData(self, load:list, imu_id:number): 
        """
        @description  : 
            function to convert data from array to IMU var
            if the imcoming data is 0 then keep the current data
        
        ---------
        @param  : 
            1. load:list -> a bytes list from scapy.sniff.packet.load. The packet should be the one transferred from Rokoko to PC
            2. id:IMU_ID -> the id of IMU, range (0, 6)
        -------
        @Returns  :
        -------
        """
        self.id = imu_id
            
        # 1. Check wether the data chunck is valid
        #   The first 4 array should be like "xx 00 00 80"
        #   The last 8 array shoule be "00"
        head_verify_ret = imu_id == int(load[0])
            
        tail_verify_ret = True
        for i in range(0,8):
            if(load[-1-i] != '00'): tail_verify_ret = False
        
        if( not(head_verify_ret and tail_verify_ret)):
            print("Error when set data of IMU:%d", imu_id)
            return False
            
        # 3. set data of imu
        data_buf = ["" for i in range(self.__data_chunk_size // self.__data_size)]
        for i in range(0, self.__data_chunk_size):
            data_buf[i//4] = load[i] + data_buf[i//4] # 高位优先           
        
        # 4 refine data of imu
        # 4.1 Remove the last part of MAG?
        for i in range(self.ACC_X, self.ACC_Z+1):
            data_buf[i] = data_buf[i][:4]
        
        #4.2 if there is 0 reading then keep the current data
        for i in range(len(data_buf)):
            if data_buf[i] != '00000000':
                self.data[i] = data_buf[i]
            
        
    def printData(self):
        print('Log IMU, id :'  + str(self.id))
        print('   acc_x = ' + self.data[self.ACC_X] + ',', end='' ) 
        print('   acc_y = ' + self.data[self.ACC_Y] + ',', end='' ) 
        print('   acc_z = ' + self.data[self.ACC_Z]) 
        print('   rot_x = ' + self.data[self.ROT_X] + ',', end='' ) 
        print('   rot_y = ' + self.data[self.ROT_Y] + ',', end='' ) 
        print('   rot_z = ' + self.data[self.ROT_Z]) 
        print('   mag_x = ' + self.data[self.MAG_X] + ',', end='' ) 
        print('   mag_y = ' + self.data[self.MAG_Y] + ',', end='' ) 
        print('   mag_z = ' + self.data[self.MAG_Z]) 
        print('   temp  = ' + self.data[self.TEMP ])  
        
    def printDataInLine(self):
        print(' acc_x = ' + self.data[self.ACC_X] + ',', end='' )
        print(' acc_y = ' + self.data[self.ACC_Y] + ',', end='' )
        print(' acc_z = ' + self.data[self.ACC_Z] + ',', end='' )
        print(' rot_x = ' + self.data[self.ROT_X] + ',', end='' )
        print(' rot_y = ' + self.data[self.ROT_Y] + ',', end='' )
        print(' rot_z = ' + self.data[self.ROT_Z] + ',', end='' )
        print(' mag_x = ' + self.data[self.MAG_X] + ',', end='' )
        print(' mag_y = ' + self.data[self.MAG_Y] + ',', end='' )
        print(' mag_z = ' + self.data[self.MAG_Z] + ',', end='' )
        print(' temp  = ' + self.data[self.TEMP ] + ',', end='' )
        print()
        
    def getDataInDecimal(self):
        out = []
        for i in range(1, self.ACC_Z + 1):
            out.append(int(self.data[i], base=16))
        return out
    
    def getData(self):
        return self.data[self.ACC_X:self.ROT_Z + 1]