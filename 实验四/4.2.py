import pandas as pd

LogInfo = pd.read_csv('Training_LogInfo.csv', encoding='gbk')
Userupdate = pd.read_csv('Training_Userupdate.csv', encoding='gbk')

# 转换时间字符串
LogInfo['Listinginfo1'] = pd.to_datetime(LogInfo['Listinginfo1'])  # 小写i
LogInfo['LogInfo3'] = pd.to_datetime(LogInfo['LogInfo3'])
print('看看LogInfo转对没：\n', LogInfo.head())

Userupdate['ListingInfo1'] = pd.to_datetime(Userupdate['ListingInfo1'])
Userupdate['UserupdateInfo2'] = pd.to_datetime(Userupdate['UserupdateInfo2'])
print('看看Userupdate转对没：\n', Userupdate.head())


# 提取用户信息更新表和登录信息表中的时间信息
# 定义一个提取用户信息的函数
def getTime(file, date):
    year = [i.year for i in file[date]]
    month = [i.month for i in file[date]]
    week = [i.week for i in file[date]]
    return year, month, week


extractedLogInfo1 = getTime(LogInfo, 'Listinginfo1')
print('表1时间信息1：\n', extractedLogInfo1[0][0:5], extractedLogInfo1[1][0:5], extractedLogInfo1[2][0:5])
extractedLogInfo2 = getTime(LogInfo, 'LogInfo3')
print('表1时间信息2：\n', extractedLogInfo2[0][0:5], extractedLogInfo2[1][0:5], extractedLogInfo2[2][0:5])

extractedUserupdate1 = getTime(Userupdate, 'ListingInfo1')
print('表2时间信息1：\n', extractedUserupdate1[0][0:5], extractedUserupdate1[1][0:5], extractedUserupdate1[2][0:5])
extractedUserupdate2 = getTime(Userupdate, 'UserupdateInfo2')
print('表2时间信息2：\n', extractedUserupdate2[0][0:5], extractedUserupdate2[1][0:5], extractedUserupdate2[2][0:5])

# 计算用户信息更新表和登录信息表中两时间的差
deltaLogInfo_day = LogInfo['Listinginfo1'] - LogInfo['LogInfo3']
deltaLogInfo_hours = deltaLogInfo_day.dt.total_seconds() / 3600.0
deltaLogInfo_minutes = deltaLogInfo_day.dt.total_seconds() / 60.0
print('表1两列时间日之差：\n', deltaLogInfo_day.head())
print('表1两列时间小时之差：\n', deltaLogInfo_hours.head)
print('表1两列时间分钟之差：\n', deltaLogInfo_minutes.head())
deltaUserupdate_day = Userupdate['ListingInfo1'] - Userupdate['UserupdateInfo2']
deltaUserupdate_hours = deltaUserupdate_day.dt.total_seconds() / 3600.0
deltaUserupdate_minutes = deltaUserupdate_day.dt.total_seconds() / 60.0
print('表2两列时间日之差：\n', deltaUserupdate_day.head())
print('表2两列时间小时之差：\n', deltaLogInfo_hours.head)
print('表2两列时间分钟之差：\n', deltaLogInfo_minutes.head())
