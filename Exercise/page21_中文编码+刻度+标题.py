from matplotlib import pyplot as plt
import random

#设置中文编码
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

x = range(0,120)
y = [random.randint(20,35)for i in range(0,120)]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#设置x轴的刻度
_xticks_labels = ["10点{}分".format(i) for i in range(0,60)]
_xticks_labels += ["11点{}分".format(i) for i in range(0,60)]

#让_xticks_labels覆盖掉x值，需要这两个列表的长度一致，并旋转45度
plt.xticks(list(x)[::6],_xticks_labels[::6],rotation=45)

#设置表格外的label
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("2小时温度趋势图")

plt.show()