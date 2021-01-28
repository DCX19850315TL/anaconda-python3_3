from matplotlib import pyplot as plt

x = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5\n：最后的骑士","摔跤吧！爸爸","加勒比海盗5\n：死无对证","金刚\n：骷髅岛","极限特工\n：终极回归","生化危机6：\n终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3\n：殊死一战","蜘蛛侠\n：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
y = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

_x = range(len(x))

#设置中文编码
plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['axes.unicode_minus'] = False

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

#绘制条形图
plt.bar(x,y,width=0.2,color='r')

#设置x轴的刻度
plt.xticks(_x,x,rotation=90)

plt.show()