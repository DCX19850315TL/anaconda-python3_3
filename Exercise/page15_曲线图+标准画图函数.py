from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

#设置图片的大小
plt.figure(figsize=(20,8),dpi=80)

#设置x轴刻度
_xticks_ = [i/2 for i in range(4,49)]
plt.xticks(_xticks_)

#绘图
plt.plot(x,y)

#保存图片
plt.savefig("./page15.png")

#显示图片
plt.show()


