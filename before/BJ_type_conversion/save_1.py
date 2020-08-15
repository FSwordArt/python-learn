from struct  import  pack
import numpy as np
import pickle

random_name = "Z_OTHE_RADAMOSAIC_201904110300_60min"

a = {0:   [[23.99, 114.91],
           [23.98, 114.90],
           [23.97, 114.92],
           [23.96, 114.93]],
     1:   [[24.99, 115.91],
           [24.98, 115.90],
           [24.97, 115.92],
           [24.96, 115.93]]
}

class strom(object):
    def __init__(self):
        self.m_nStormCount = 0
        self.m_nStormBoundaryPointNum = 0
        self.lonlat = []

class m_DateTime(object):
    def __init__(self):
        self.m_storm = []
        self.m_nYear = []
        self.m_nMonth = []
        self.m_nDay = []
        self.m_nHour = []
        self.m_nMinute = []

def save_titan(path):

    name = b"NMCTITAN"
    version = 1
    tt = b"                "

    m_DateTime.m_nYear = int(path[-18:-14])
    m_DateTime.m_nMonth = int(path[-14:-12])
    m_DateTime.m_nDay = int(path[-12:-10])
    m_DateTime.m_nHour = int(path[-10:-8])
    m_DateTime.m_nMinute = int(path[-8:-6])
    nTrackTimeCount = 0
    nForecastCount = 1
    nForecastMinute = int(path[-5:-3])
    nStormCount = 2  # 风暴个数

    m_Strom = []
    m_Storm[ii].m_storm.append(storm())
    for ks, vs in a.items():
        ar_vs = np.array(vs)
        ar_vs[:, [0, 1]] = ar_vs[:, [1, 0]]

    #     m_Strom.append(ar_vs)
    # print(m_Strom)
    # for ii in range(nForecastCount):
    #     m_Strom.append(strom())
    #     m_Strom[ii].m_nStormCount = 2


        for jj in range(m_Strom[ii].m_nStormCount):
            m_Strom[ii].m_nStormCount[jj].append(ar_vs)

    print(m_Strom)


if __name__ == '__main__':
    save_titan(random_name)






