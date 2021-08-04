import collections
import pandas

for i in range(7):
    lottery_drawing = pandas.Series(['no luck', 'first prize'])

    # 利用Ture sample进行有放回随机抽样
    # 利用Counter计算两个值分别的取值个数
    temp = collections.Counter(lottery_drawing.sample(n=100, replace=True, weights=([99, 1])))

    print(temp)
