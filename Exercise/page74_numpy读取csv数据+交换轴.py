import numpy as np

US_data = np.loadtxt('./youtube_video_data/US_video_data_numbers.csv',dtype=int,delimiter=',',unpack=1)
#print(data)


a = np.array(range(20)).reshape(4,5)
print(a)
#数组的转置，将行和列进行调换
a = a.transpose()
print(a)