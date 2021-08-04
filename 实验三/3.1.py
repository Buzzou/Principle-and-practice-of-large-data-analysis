# 人口数据特征间的关系
import os
import numpy as np
import matplotlib.pyplot as plt

# 用numpy读人口数据
os.chdir('/Users/ruohaoli/PycharmProjects/Data_Analysis')
plt.rcParams['font.sans-serif'] = ['HanziPen SC']  # 设置中文显示
feature = np.load('populations.npz', allow_pickle=True)['feature_names']  # 加载列名
amount = np.load('populations.npz', allow_pickle=True)['data']  # 加载数据

# 散点图
p1 = plt.figure(figsize=(20, 10))  # 创建空白画布，宽高，英尺
ax1 = p1.add_subplot(2, 1, 1)  # 创建并选中第一幅子图，行，列，选中图片编号
plt.title('1996-2015年人口数据散点图与折线图 ')  # 当前图形标题，名称等
plt.ylabel('人口数量 ')  # 当前图形y名，等
plt.xticks(rotation=45)  # x轴刻度位置和值
for i in range(1, 6):  # 利用 for循环画散点图
    plt.scatter(amount[:, 0][0:20], amount[:, i][0:20])  # x轴y轴数据
ax1.legend(feature[1:], bbox_to_anchor=(1, 1), ncol=1)  # 图例相对轴位置，几列图

# 折线图
ax2 = p1.add_subplot(2, 1, 2)  # 创建并选中第二幅子图，行，列，选中图片编号
plt.ylabel('人口数量 ')  # 当前图形y名，等
plt.xticks(rotation=45)  # x轴刻度位置和值
for i in range(1, 6):
    plt.plot(amount[:, 0][0:20], amount[:, i][0:20])  # x轴y轴数据
ax2.legend(feature[1:], bbox_to_anchor=(1, 1), ncol=1)  # 图例相对轴位置，几列图

# 显示图片
plt.show()
