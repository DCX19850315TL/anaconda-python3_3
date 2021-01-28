from matplotlib import pyplot as plt

y3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

#因为要使用散点图，并且在一张图上进行显示，需要分别设置x轴进行对比
x3 = range(1,32)
x10 = range(51,82)

#设置中文编码
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

#设置图形的大小
plt.figure(figsize=(20,8),dpi=80)

#设置x和y轴的刻度
_x = list(x3) + list(x10)
_xticks_labels = ["3月{}日".format(i) for i in x3]
_xticks_labels += ["10月{}日".format(i-50) for i in x10]
_yticks_labels = range(0,35)

plt.yticks(_yticks_labels)
plt.xticks(_x,_xticks_labels,rotation=45)

#设置散点图
plt.scatter(x3,y3,label="三月份")
plt.scatter(x10,y10,label="十月份")

#增加图例
plt.legend(loc="upper left")

#增加网格
plt.grid(alpha=1,linestyle=':')

#增加x,y轴说明和title
plt.xlabel("月份")
plt.ylabel("温度")
plt.title("3月份和10月份温度比较")

#显示图形
plt.show()