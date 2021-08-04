# 人口数据各个特征的分布与分散状况
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/ruohaoli/PycharmProjects/Data_Analysis')
plt.rcParams['font.sans-serif'] = ['HanziPen SC']  # 设置中文显示
feature = np.load('populations.npz', allow_pickle=True)['feature_names']  # 加载列名
amount = np.load('populations.npz', allow_pickle=True)['data']  # 加载数据

# 直方图
p1 = plt.figure(figsize=(18, 9))  # 创建第一幅空白画布，宽高，英尺
ax1 = p1.add_subplot(2, 1, 1)  # 创建并选中第一幅子图，行，列，选中图片编号
plt.title('1996-2015年男女人口及乡镇人口数目直方图')  # 当前图形标题，名称等
plt.ylabel('人口数量')  # 当前图形y名，等
plt.bar(np.arange(22), amount[:, 2], width=0.3)  # x轴数据，柱形图高，直方图宽度
plt.bar(np.arange(22) + 0.3, amount[:, 3], width=0.3)  # x轴数据，柱形图高，直方图宽度
plt.xticks(np.arange(22), amount[:, 0], rotation=45)  # x轴刻度位置和值
ax1.legend(feature[2:4], bbox_to_anchor=(1, 1), ncol=1)  # 图例相对轴位置，几列图

ax2 = p1.add_subplot(2, 1, 2)  # 创建并选中第二幅子图，行，列，选中图片编号
plt.ylabel('人口数量')  # 当前图形y名，等
plt.bar(np.arange(22), amount[:, 4], width=0.3)  # x轴数据，柱形图高，直方图宽度
plt.bar(np.arange(22) + 0.3, amount[:, 5], width=0.3)  # x轴数据，柱形图高，直方图宽度
plt.xticks(range(22), amount[:, 0], rotation=45)  # x轴刻度位置和值
ax2.legend(feature[4:6], bbox_to_anchor=(1, 1), ncol=1)  # 图例相对轴位置，几列图

plt.savefig('直方图.png')  # 保存图片
plt.show()  # 本机显示图形

# 饼图
i = 0
L = 1
p2 = plt.figure(figsize=(4, 44))  # 创建空白画布，宽高，英尺
while i < 20:
    pie1 = p2.add_subplot(20, 2, L)
    label = ['男', '女']
    explode = [0.01, 0.01]
    plt.pie(amount[19 - i, 2:4], explode=explode, labels=label, autopct='%1.1f%%')  # 源数据，某项离圆心有多少单位半径，各项名称，数值显示方式
    plt.title('%d年男女与城乡人口比例' % (1996 + i))  # 当前图形标题，名称等
    i += 1
    L += 2

j = 0
k = 2
while j < 20:
    pie1 = p2.add_subplot(20, 2, k)
    label = ['城镇人口', '乡村人口']
    explode = [0.01, 0.01]
    plt.pie(amount[19 - j, 4:6], explode=explode, labels=label, autopct='%1.1f%%')  # 源数据，某项离圆心有多少单位半径，各项名称，数值显示方式
    j += 1
    k += 2

plt.show()  # 本机显示图形

plt.savefig('饼图.png')  # 保存图片
plt.show()  # 本机显示图形

# 箱线图
plt.figure(figsize=(18, 9))  # 创建第三幅空白画布，宽高，英尺
label = ['年末总人口', '男性人口', '女性人口', '城镇人口', '乡村人口']
population = (amount[:, 1], amount[:, 2], amount[:, 3], amount[:, 4], amount[:, 5])
plt.boxplot(population, notch=True, labels=label, meanline=True)  # 源数据，中间箱体有缺口，各箱线图标签，显示均值线
plt.title('1996~2015年人口变化箱线图')  # 当前图形标题，名称等
plt.ylabel('人口数量(万人)')  # 当前图形y名，等

plt.savefig('箱线图.png')  # 保存图片
plt.show()  # 本机显示图形
