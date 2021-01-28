from matplotlib import pyplot as plt

#设置中文编码
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

x = range(11,31)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

plt.plot(x,y)

_yticks_labels = range(0,9)
_xticks_labels = ["{}岁".format(i) for i in x]

plt.xticks(x,_xticks_labels,rotation=45)
plt.yticks(_yticks_labels)

#增加网格，alpha为表格线的粗细程度
plt.grid(alpha=0.3)

plt.show()