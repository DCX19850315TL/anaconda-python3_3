import numpy as np

t1 = np.array(range(20)).reshape(2,10)
t2 = np.array(range(20,40)).reshape(2,10)

#竖直拼接
new1 = np.vstack((t1,t2))

#水平拼接
new2 = np.hstack((t1,t2))

