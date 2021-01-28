from matplotlib import pyplot as plt

#设置中文编码
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

plt.figure(figsize=(20,8),dpi=80)

#由于数据经过了处理，不能用直方图，需要用条形图展示
plt.bar(range(12),quantity,width=1)

#设置x轴的刻度,_x的目的是将条形图连接到一起，形成直方图的样子
_x = [i-0.5 for i in range(13)]
_xtick_labels =  interval+[150]
plt.xticks(_x,_xtick_labels)

plt.show()