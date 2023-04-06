from wsgiref.headers import tspecials
import pandas as pd
import numpy as np
import torch 

# # Index test
# src = [str(i) for i in range(16)]
# out = ""
# for i in range(0,8):
#     out = src[-1-i] + out
# print(out)

'''
combine list
'''
# a = [1,2,3]
# b = [4,5,6]
# print(a+b)

'''
append pandas row
'''
# df_head = ['a','b','c']
# df = pd.DataFrame(columns=df_head)

# data = [1,2,3]
# df.loc[len(df.index)] = data

# print(df)

'''
append pandas rows
'''
# df_head = ['a','b','c']
# df = pd.DataFrame(columns=df_head)

# # Append rows
# data = [1,3,5]
# df.loc[len(df.index)] = data
# data = [2,4,6]
# df.loc[len(df.index)] = data

# # append cols 即df.insert(添加列位置索引序号，添加列名，数值，是否允许列名重复)
# df.insert(len(df.columns), 'append', 0, False)


'''
Pandas select some row
'''
# df_head = ['a','b','c']
# df = pd.DataFrame(columns=df_head)
# data = [1,4,7]
# df.loc[len(df.index)] = data
# data = [2,5,8]
# df.loc[len(df.index)] = data
# data = [3,6,9]
# df.loc[len(df.index)] = data

# print(df.loc[0:0])
# print('Len of dataframe = ' + str(len(df)))


'''
Pandas clear data method
'''
# df_head = ['a','b','c']
# df = pd.DataFrame(columns=df_head)
# data = [1,4,7]
# df.loc[len(df.index)] = data
# data = [2,5,8]
# df.loc[len(df.index)] = data
# data = [3,6,9]
# df.loc[len(df.index)] = data

# df.drop(df.index, inplace=True)
# print(df)

'''
死妈问题
Pandas to tensor
'''
# df_head = ['a','b','c']
# df = pd.DataFrame(columns=df_head)
# data = [1,4,7]
# df.loc[len(df.index)] = data
# data = [2,5,8]
# df.loc[len(df.index)] = data
# data = [3,6,9]
# df.loc[len(df.index)] = data

# data = np.array(df[0:2])
# ts = torch.from_numpy(data)
# print(ts)

'''
Calculate Char
'''
# char = 'A'
# char = ord(char) + 1
# print(chr(char))


'''
Pandas and Numpy.argmax
'''

# data = tensor([1,4,7])

# print(np.argmax(data))

'''
Add col to pandas
'''
# df_head = ['a','b','c']
# df = pd.DataFrame(columns=df_head)
# data = [1,4,7]
# df.loc[len(df.index)] = data
# data = [2,5,8]
# df.loc[len(df.index)] = data
# data = [3,6,9]
# df.loc[len(df.index)] = data

# a = df['a']
# b = df['b']

# d = a**2 + b**2
# df.insert(len(df.columns), 'd', d, False)

# print(df)

'''
Push and pop of list
'''
list = [1,2,3]
list.append(4)
list.pop(0)
print(list)