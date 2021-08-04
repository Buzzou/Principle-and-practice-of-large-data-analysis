import pandas as pd

LogInfo = pd.read_csv('Training_LogInfo.csv', encoding='gbk')
Userupdate = pd.read_csv('Training_Userupdate.csv', encoding='gbk')

# 用pivot_table函数将长表转换成宽表
covertedLogInfo = pd.pivot_table(LogInfo, index='Idx', columns=['LogInfo1'], aggfunc='count')
print('透视登录信息表：\n', covertedLogInfo.head())
covertedUserupdate = pd.pivot_table(Userupdate, index='Idx', columns=['UserupdateInfo1'], aggfunc='count')
print('透视用户信息更新表：\n', covertedUserupdate.head())
