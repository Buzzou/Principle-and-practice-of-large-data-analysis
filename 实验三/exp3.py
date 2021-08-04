import numpy as np
import matplotlib.pyplot as plt


def draw_data():
    data = np.load("populations.npz", allow_pickle=True)
    # data.files查看文件具体内容
    # array(['时间', '年末总人口(万人)', '男性人口(万人)', '女性人口(万人)', '城镇人口(万人)', '乡村人口(万人)'],
    #  dtype=object)
    # 数据最后两行为nan
    population = data['data']
    time = population[:-2, 0]
    totalpopl = population[:-2, 1]
    menpopl = population[:-2, 2]
    womenpopl = population[:-2, 3]
    citypopl = population[:-2, 4]
    ruralpopl = population[:-2, 5]

    # 绘图
    import matplotlib
    matplotlib.rcParams['font.sans-serif'] = ['HanziPen SC']  # 指定默认字体
    matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    fig, subplot_arr = plt.subplots(2, 1, figsize=(20, 20))
    subplot_arr[0,].scatter(time[::-1], menpopl[::-1], marker='o', label='男性人口(万人)')
    subplot_arr[0,].scatter(time[::-1], womenpopl[::-1], marker='D', label="女性人口(万人)")
    subplot_arr[1,].scatter(time[::-1], citypopl[::-1], marker='o', label='城镇人口(万人)')
    subplot_arr[1,].scatter(time[::-1], ruralpopl[::-1], marker='D', label="乡村人口(万人)")
    subplot_arr[0,].set_xlabel("时间")
    subplot_arr[0,].set_ylabel("人口数量")
    subplot_arr[0,].legend(loc='best')
    subplot_arr[0,].set_title("男女人口对比")
    subplot_arr[1,].set_xlabel("时间")
    subplot_arr[1,].set_ylabel("人口数量")
    subplot_arr[1,].legend(loc='best')
    subplot_arr[1,].set_title("城乡人口对比")
    plt.savefig('./题目1散点图.jpg')  # 保存图片
    plt.show()  # 本机显示图形


def main():
    draw_data()


if __name__ == '__main__':
    main()
