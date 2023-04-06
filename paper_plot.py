from matplotlib import pyplot as plt
import pandas as pd
from data_analyze import appendAccNormCol

RESOLUTION = 40

data = pd.read_csv('./csv/20_home_test/data_3.csv')

appendAccNormCol(data)
plot_data = data[['acc_norm_0', 'acc_norm_1',  'acc_norm_2',   'acc_norm_3',   'acc_norm_4',   'acc_norm_5']]
data = data.iloc[60: 60 + RESOLUTION]
x_axis = [i for i in range(RESOLUTION)]


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Hammer')
ax.set_xlabel('sequence num')
ax.set_ylabel('Imu Val')
for i in range(len(plot_data.columns)):
    head = 'acc_norm_' + str(i)
    label = 'imu_' + str(i)
    ax.plot(x_axis, data[head],label=label)
    ax.legend()
plt.show()