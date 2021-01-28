import numpy as np

a = np.array(range(12)).reshape(3,4)
print(a)

#取第二行的数据
print(a[1])

#取所有行的第2列
print(a[:,1])

#取第二行和第三行的数据，连续
print(a[1:3])

#取所有行的第2列和第3列，连续
print(a[:,1:3])

#取第一行和第三行的数据，不连续
print(a[[0,2],:])

#去第二列和第四列的数据，不连续
print(a[:,[1,3]])

#将所有行的第2列和第三列的值改为0
a[:,1:3] = 0
print(a)

#查看小于5的有哪些
print(a<5)

#将小于5的值改为123
a[a<5]=123
print(a)

#将小于10的值变为0，将大于10的值变为111
print(np.where(a<10,0,111))

#将小于10的值变为10，将大于25的值变为25
b = np.array(range(28)).reshape(4,7)
print(b.clip(10,25))

#设置一个正无穷的数
#inf(-inf,inf):infinity,inf表示正无穷，-inf表示负无穷
#什么时候回出现inf包括（-inf，+inf）比如一个数字除以0，（python中直接会报错，numpy中是一个inf或者-inf）
c = np.inf
print(type(c))

#设置一个nan
#not a number表示不是一个数字
#什么时候numpy中会出现nan：当我们读取本地的文件为float的时候，如果有缺失，就会出现nan当做了一个不合适的计算的时候(比如无穷大(inf)减去无穷大)
#nan和任何数值计算结果都是nan
d = np.nan

#两个nan的数不相等
print(np.nan==np.nan)

#生成nan的数组,使用np.nan赋值为nan,必须保证原始数值的类型为float
e = np.array(range(32),dtype=float).reshape(4,8)
e[1] = np.nan
print(e)

#判断数组中nan的个数
print(np.count_nonzero(e!=e))

#判断数组中的数值是否是nan
print(e[np.isnan(e)])

#判断数组中的数值是否是nan，如果是nan的替换为0
e[np.isnan(e)]=0
print(e)

#对数组中的行和列进行计算
f = np.array(range(30)).reshape(3,10)
print(f)
#计算每列的总和
print(f.sum(axis=0))
#计算每行的总和
print(f.sum(axis=1))
#计算每列的均值
print(f.mean(axis=0))
#计算每列的中值
print(np.median(f,axis=0))
#计算每列的最大值
print(f.max(axis=0))
#计算每列的最小值
print(f.min(axis=0))
#极值：np.ptp(t,axis=None) 即最大值和最小值只差
print(np.ptp(f,axis=0))
#每列的标准差:Exercise/标准差计算公式.png
print(f.std(axis=0))

#将数组中的nan填充为
g = np.array(range(32),dtype=float).reshape(4,8)
g[1] = np.nan
print(g)

def fill_nan_by_colum_mean(t):
    for i in range(t.shape[1]):
        #求出每列包含nan的个数
        nan_num = np.count_nonzero(t[:,i]!=t[:,i])
        if nan_num > 0:
            now_col = t[:,i]
            #求出每列非nan的数值的和
            now_col_not_nan = now_col[np.isnan(now_col) == False].sum()
            #每列的总和除以每列非nan的个数=(每列的个数减去每列nan的个数)
            now_col_mean = now_col_not_nan / (t.shape[0] - nan_num)
            #将每列为nan的值替换为求出的均值
            now_col[np.isnan(now_col)] = now_col_mean
            #将新生成的每列数据重新进行赋值
            t[:,i] = now_col
    return t
print(fill_nan_by_colum_mean(g))