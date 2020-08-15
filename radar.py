import os, datetime
import matplotlib.pyplot as plt
import numpy as np
from struct import *
import bz2
from datetime import datetime, timedelta
from scipy.ndimage import filters

############## config #####################
# 雷达经纬度信息，默认尺寸：4200*6200
# 全尺寸坐标
fLeftLon = 73.0
fRightLon = 135.0
fTopLat = 54.2
fButtomLat = 12.20
fLonReso = 0.01
fLatReso = 0.01

# 自定义坐标
MyLeftLon = 114.74
MyRightLon = 119.86
MyTopLat = 41.56
MyButtomLat = 36.44
#########################################

def readradar(radarpath,file):
    # 当前时刻不存在， 就用下一时刻或者上一时刻，间隔6min
    # 读取数据
    f = bz2.BZ2File(radarpath + file, 'rb')
    # f = open(radarpath + file, 'rb')
    f.seek(204)
    rows = unpack('i', f.read(4))[0] # 行列数
    cols = unpack('i', f.read(4))[0]
    radardata = cols * rows * [-999.999]
    f.seek(224)
    levelbytes = unpack('i', f.read(4))[0]
    f.seek(256)
    data = unpack('%dh' % (levelbytes/2), f.read(levelbytes)) # 短整型 2个字节
    Y = data[0]
    X = data[1]
    N = data[2]
    index = 3
    while Y >= 0 and X >= 0 and N >= 0:
        for i in range(N):
            radardata[(4200 - Y) * cols + X] = data[index]
            X = X + 1
            index = index + 1
        Y = data[index]
        index = index + 1
        X = data[index]
        index = index + 1
        N = data[index]
        index = index + 1
    result = np.array(radardata)
    f.close()
    result[result<0]=0
    result = result.reshape(4200, 6200)/10
    print(result.shape)

    # result = filters.median_filter(result, 5)
    top = int((MyButtomLat - fButtomLat) / fLatReso)
    buttom = int((MyTopLat - fButtomLat) / fLatReso)
    left = int(round(MyLeftLon - fLeftLon,2) / fLonReso)
    right = int((MyRightLon - fLeftLon) / fLonReso)
    return result[top:buttom, left:right]

if __name__ == '__main__':
    # radarpath = 'E:/work/radar_data/'
    # data=readradar(radarpath, 'ACHN.CREF000.20170309.112400.latlon.bz2')
    root = "C:/Users/Yunlong/Desktop/radar/"
    path = os.listdir(root)
    for file in path:
        print(file)
        data = readradar(root, file)
        print(data.shape)
        print(file[13:26])
        np.save("C:/Users/Yunlong/Desktop/npy/" + file[13:26] + ".npy", data)

    # plt.imshow(data)
    # #plt.contourf(data)
    # plt.colorbar()
    # plt.show()