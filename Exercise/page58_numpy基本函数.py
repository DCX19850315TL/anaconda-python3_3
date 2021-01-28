import numpy as np
import random

a = np.array([1,2,3,4,5])
b = np.array(range(1,6))
c = np.arange(1,6)

print(a,b,c)

print(type(a))

print(a.dtype)
print(c.dtype)

#设置类型为布尔类型
d = np.array([1,0,1,0],dtype=np.bool)
print(d)
#将类型修改为int8
d = d.astype(np.int8)
print(d)

e = np.array([1.311111111,3.3333333333],dtype=np.float64)
print(e)
#截取小数点后2位
e = e.round(2)
print(e)

f = np.array([[0,1,2,3,4,5],[5,6,7,8,9,10]])
print(f)
#数组的结构
print(f.shape)
#重新定义数组的结构
print(f.reshape(3,4))
#真正将f的2行6列数组修改为3行4列
g = f.reshape(3,4)
print(g)
#将多维数组修改为一维数组
print(g.flatten())

h = np.array([[0,1,2,3,4,5],[5,6,7,8,9,10]])
#数和数组的计算是广播的，所有元素都进行了计算
print(h+1)
print(h*3)

#数组与数组的计算也是广播的
i = np.array([[10,11,12,13,14,15],[15,16,17,18,19,110]])
j = np.array([[0,1,2,3,4,5],[5,6,7,8,9,10]])
print(i+j)
print(i*j)

#不同维度的数组之间的计算,需要保证其中一组的数据为一维数组
k = np.array([10,11,12,13])
l = np.array([[10,11,12,13,14,15],[15,16,17,18,19,110],[15,16,17,18,19,110],[15,16,17,18,19,110]])
l = l.reshape(6,4)
print(l)
print(k+l)

m = np.array([[10,11,12,13],[1,2,3,4]])
n = np.array(range(2)).reshape(2,1)
print(n)
print(m+n)

