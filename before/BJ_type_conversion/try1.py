import struct
import os
import numpy as np

class Titan_Storm(object):
    def __init__(self):
        self.m_nStormCount = 0
        # self.m_nStormBoundaryPointNum = []
        class FPOINT:
            def __init__(self):
                self.lon = []
                self.lat = []
Titan_Storm.
# class FPOINT(object):
#     def __init__(self):
#         self.lon = []
#         self.lat = []

# class m_nStormBoundaryPoint(Titan_Storm):
#     def __init__(self):
#         Titan_Storm.__init__(self)
#         self.lon = []
#         self.lat = []

class m_DateTime(object):
    def __init__(self):
        self.m_storm = []
        self.m_nYear = []
        self.m_nMonth = []
        self.m_nDay = []
        self.m_nHour = []
        self.m_nMinute = []
        self.m_nSecond = []

c = {0:   [[23.99, 114.91],
           [23.98, 114.90],
           [23.97, 114.92],
           [23.96, 114.93]],
     1:   [[24.99, 115.91],
           [24.98, 115.90],
           [24.97, 115.92],
           [24.96, 115.93]]
}
def save_titan(path):
# def save_titan(year,month,day,hour,minute,num,nforecastminute,nstormboundarypointnum):
    name = "NMCTITAN"
    version = 1
    tt = " "
    m_datetime = m_DateTime()
    m_datetime.m_nYear = path[0][-20, -17]
    m_datetime.m_nMonth = path[0][-16, -15]
    m_datetime.m_nDay = path[0][-14, -13]
    m_datetime.m_nHour = path[0][-12, -11]
    m_datetime.m_nMinute = path[0][-10, -9]
    m_datetime.m_nSecond = path[0][-8, -7]
    save_lon = []
    save_lat = []
    save_lonlat = []

    # Year = int(year)
    # Month = int(month)
    # Day = int(day)
    # Hour = int(hour)
    # Minute =int(minute)
    # nTrackTimeCount = 0
    # nForecastCount = 1   #有多少个预测的圈
    # nForecastMinute = nforecastminute #预报的时间，我们为30min或60min
    # nStormCount = num #风暴个数
    # # nStormBoundaryPointNum = nstormboundarypointnum

    for ks, vs in c.items():
        print(ks)
        # for v in vs:
        print(vs)
        ar_vs = np.array(vs)
        print(ar_vs)
        save_lon = ar_vs[:, 1]
        save_lat = ar_vs[:, 0]

        # save_lon = np.array(save_lon.reshape(-1, 1))
        # save_lat = np.array(save_lat.reshape(-1, 1))
        # save_lonlat = np.concatenate(save_lon, save_lat)

        print("save_lon", save_lon)
        print("save_lat", save_lat)
        # print(save_lonlat)


if __name__ == '__main__':
    save_titan()