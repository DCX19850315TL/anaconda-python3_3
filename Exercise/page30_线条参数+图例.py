from matplotlib import pyplot as plt

x = range(11,31)
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
y_max = max(y1 + y2) + 2
print(y_max)

#设置中文编码
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

#设置x轴的刻度
_xticks_labels = ["{}岁".format(i) for i in x]
_yticks_labels = range(0,y_max)

plt.xticks(x,_xticks_labels)
plt.yticks(_yticks_labels)

#增加线条的标签，颜色和线条样式
plt.plot(x,y1,label="自己",color="#F08080")
plt.plot(x,y2,label="他人",linestyle="--")

#添加图例在右上角
plt.legend(loc="upper right")

#增加表格，透明度为1，线条为:
plt.grid(alpha=1,linestyle=':')

#增加x,y轴名称和title
plt.xlabel('岁数')
plt.ylabel('交往个数')
plt.title('20年间两人交往女朋友的个数')

plt.show()

