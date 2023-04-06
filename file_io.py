import csv

import pandas as pd

def fileAppend(path, data):
    '''
    Function to append data to a file
    If the file is not existed, a new one will be created
    '''
    file = open(path, 'a')
    file.writelines(data + "\n")
    file.close()
    
        
def writeDataFrame(path, dataFrame:pd.DataFrame):
    '''
    Save pandas.DataFrame to csv
    '''
    with open(path, 'w', newline='') as f:
        csv_write = csv.writer(f)
        
        data_row = dataFrame.columns
        csv_write.writerow(data_row)
        csv_write.writerows(dataFrame.values)
            
def appendDataFrame(path, dataFrame:pd.DataFrame):
    '''
    Append pandas.DataFrame to an existed csv
    '''
    with open(path,'a', newline='') as f:
        csv_write = csv.writer(f)

        csv_write.writerows(dataFrame.values)