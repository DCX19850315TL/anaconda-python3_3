# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels)
plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=1)

#设置title和x,y轴说明
plt.xlabel("岁数")
plt.ylabel("交往女朋友的个数")
plt.title("每年交往女朋友个数趋势图")

#展示
plt.show()
