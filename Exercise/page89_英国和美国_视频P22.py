import numpy as np

us_data_path = './youtube_video_data/US_video_data_numbers.csv'
gb_data_path = './youtube_video_data/GB_video_data_numbers.csv'

us_data = np.loadtxt(us_data_path,dtype=int,delimiter=',',unpack=0)
gb_data = np.loadtxt(gb_data_path,dtype=int,delimiter=',',unpack=0)

#视频点击数，喜欢，不喜欢，评论数量
#英国评论数量
x = gb_data[:,-1]

#组距


print(max(x))
print(min(x))