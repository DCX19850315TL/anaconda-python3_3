from matplotlib import pyplot as plt

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

#设置中文编码
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

width = 0.2

#设置x轴的长度
x14 = range(len(a))
x15 = [i+width for i in x14]
x16 = [i+width*2 for i in x14]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

#绘制条形图
plt.bar(x14,b_14,label='9月14日',width=width)
plt.bar(x15,b_15,label='9月15日',width=width)
plt.bar(x16,b_16,label='9月16日',width=width)

#x轴刻度
plt.xticks(x15,a)

#设置图例
plt.legend()

plt.show()
