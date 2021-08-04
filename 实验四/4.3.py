import pandas as pd
import numpy as np

LogInfo = pd.read_csv('Training_LogInfo.csv', encoding='gbk')
Userupdate = pd.read_csv('Training_Userupdate.csv', encoding='gbk')

# 使用groupby方法对用户信息更新表和登录信息表进行分组
groupedLogInfo = LogInfo[['Idx', 'LogInfo3']].groupby(by='Idx')
groupedUserupdate = Userupdate[['Idx', 'UserupdateInfo2']].groupby(by='Idx')

# 使用agg方法求取分组后的最早，最晚，更新登录时间
print('最早登录时间：\n', groupedLogInfo.agg(np.min))
print('最晚登录时间：\n', groupedLogInfo.agg(np.max))
print('最早更新时间：\n', groupedUserupdate.agg(np.min))
print('最晚更新时间：\n', groupedUserupdate.agg(np.max))

# 求取分组后的数据的信息更新次数与登录次数
print('数据信息更新次数：\n', groupedLogInfo.size())
print('数据登录次数：\n', groupedUserupdate.size())
