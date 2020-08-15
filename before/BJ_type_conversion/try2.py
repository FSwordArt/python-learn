# coding=utf-8
import struct
from struct import pack
import os
import numpy as np

class storm(object):
 def __init__(self):
  self.m_nStormCount = 0
  self.m_nStormBoundaryPointNum = 0
  self.lat = ""
  self.lon = ""
  self.latlon = []

class m_DateTime(object):
    def __init__(self):
        self.m_storm = []
        self.m_nYear = 0
        self.m_nMonth = 0
        self.m_nDay = 0
        self.m_nHour = 0
        self.m_nMinute = 0
        self.m_Second = 0
        self.m_nStormCount = 0




random_name = "Z_OTHE_RADAMOSAIC_201904110448_30min"
cot = {0: [[24.026, 114.318], [24.042, 114.314], [24.06, 114.310]],
     1: [[24.146, 115.158], [24.162, 115.154], [24.180, 115.150]],
     2: [[24.146, 113.538], [24.162, 113.534], [24.172, 113.524]],
     3: [[27, 117], [27.1, 117.1], [27.2, 117.2], [27.3, 117.3], [27.4, 117.4]]}
c = 4

def save_titan(path):
    m_datatime = m_DateTime()
    filepath = 'D:/pcprogram/type_conversion/save_bin/' + str(random_name) + '.bin'
    with open(filepath, 'wb') as fid:

        TITAN_flag = b"NMCTITAN"
        m_nVersion = 1
        t = b"                "
        m_datatime.m_nYear = int(random_name[-18:-14])
        m_datatime.m_nMonth = int(random_name[-14:-12])
        m_datatime.m_nDay = int(random_name[-12:-10])
        m_datatime.m_nHour = int(random_name[-10:-8])
        m_datatime.m_nMinute = int(random_name[-8:-6])
        m_datatime.m_nSecond = 0
        m_nTrackTimeCount = 0
        m_nForecastCount = 1
        nForecastMinute = int(random_name[-5:-3])    # 预报的时间是30min或60min
        nStormCount = c    # 预测的风暴个数

        args_temp = [TITAN_flag, m_nVersion, t,
                     m_datatime.m_nYear, m_datatime.m_nMonth, m_datatime.m_nDay,
                     m_datatime.m_nHour, m_datatime.m_nMinute, m_datatime.m_nSecond,
                     m_nTrackTimeCount, m_nForecastCount, nForecastMinute, nStormCount]
        args = tuple(args_temp)  # 把列表转换为元组
        all = struct.pack("<8si16s2H4B4i", *args)

        fid.write(all)
        ##############
        #############
        m_Storm = []
        for ii in range(m_nForecastCount):
            m_Storm.append(m_DateTime())
            m_Storm[ii].m_nYear = int(random_name[-18:-14])
            m_Storm[ii].m_nMonth = int(random_name[-14:-12])
            m_Storm[ii].m_nDay = int(random_name[-12:-10])
            m_Storm[ii].m_nHour = int(random_name[-10:-8])
            m_Storm[ii].m_nMinute = int(random_name[-8:-6])
            m_datatime.m_nSecond = 0
            m_Storm[ii].m_nStormCount = nStormCount
            args_temp_2 = [m_Storm[ii].m_nYear, m_Storm[ii].m_nMonth, m_Storm[ii].m_nDay, m_Storm[ii].m_nHour, m_Storm[ii].m_nMinute, m_Storm[ii].m_nStormCount]
            args2 = tuple(args_temp_2)
            all2 = struct.pack("<2H3Bi", *args2)
            fid.write(all2)

            # m_Storm[ii].m_storm.append(storm())
            for key, value in cot.items():
                m_Storm[ii].m_storm.append(storm())
                # print(key)
                # print(len(value))
                # print(value)
                m_Storm[ii].m_storm[key].m_nStormBoundaryPointNum = len(value)
                # print(m_Storm[ii].m_storm[key].m_nStormBoundaryPointNum)

                arr = np.array(value)
                arr[:, [0, 1]] = arr[:, [1, 0]]
                print(arr)

                for i in range(len(arr)):

                    m_Storm[ii].m_storm[key].lon = pack('f', arr[i][0])
                    m_Storm[ii].m_storm[key].lat = pack('f', arr[i][1])

                    fid.write(m_Storm[ii].m_storm[key].lon)
                    fid.write(m_Storm[ii].m_storm[key].lat)



if __name__ == '__main__':
    save_titan(random_name)
