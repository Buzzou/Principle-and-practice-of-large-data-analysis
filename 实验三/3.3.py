import numpy as np
import matplotlib.pyplot as plt
from pandas import *

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
data = read_csv('/Users/ruohaoli/PycharmProjects/Data_Analysis/TopBabyNamesbyState.csv')
State = data['State'].tolist()
Gender = data['Gender'].tolist()
Year = data['Year'].tolist()
Name = data['Top Name'].tolist()
Occurences = data['Occurences'].tolist()
print('Occurences:', Occurences)

plt.figure(figsize=(206, 206))
plt.bar(np.arange(206), height=Occurences, width=0.5)
plt.xlabel('年份')
plt.ylabel('使用次数')
plt.xticks(range(206), Year)
plt.title('Top Baby Name in the State of AK')
plt.savefig('/Users/ruohaoli/PycharmProjects/Data_Analysis/TopBabyNamesbyState.png')
plt.show()
