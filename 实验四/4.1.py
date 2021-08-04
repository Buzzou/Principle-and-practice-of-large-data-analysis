import pandas as pd

data = pd.read_csv('Training_Master.csv', encoding='gbk')
print('维度：', data.ndim)
print('行列数：', data.shape)
print('占用内存：\n', data.memory_usage)

# 使用describe方法进行描述性统计
print('描述性统计：\n', data.describe())


# 剔除值相同（标准差为0）或全为空的列
def reject(data):
    numOfColumn = data.shape[1]
    notNull = data.describe().loc['count'] == 0  # 非空值数目
    for i in range(len(notNull)):
        if notNull[i]:
            data.drop(notNull.index[i], axis=1, inplace=True)  # 删列，直接替换

    sameValue = data.describe().loc['std'] == 0  # 标准差为0
    for i in range(len(sameValue)):
        if sameValue[i]:
            data.drop(sameValue.index[i], axis=1, inplace=True)
    delta = data.shape[1]
    print('去除的列的数目为：', numOfColumn - delta)
    print('去除后数据的形状为：', data.shape)


reject(data)
