import os
import numpy as np
import struct

r_f = os.listdir('F:/TITAN_BJ/Save_Titan')
# domain = os.path.abspath('F:/TITAN_BJ/Save_Titan') #获取文件夹的路径，此处其实没必要这么写，目的是为了熟悉os的文件夹操作
FP = 'F:/TITAN_BJ/Save_Titan'
data = ""

for info in os.listdir('F:/TITAN_BJ/Save_Titan'):
    print(info)
    info = os.path.join(FP, info)  # 将路径与文件名结合起来就是每个文件的完整路径
    print(info)
    with open(info, 'rb') as f:
        data = struct.unpack("<8si16s2H3B4i", f[-40:])

    result = str(data)
    f.close()


for file in r_f:
    print(file)
    filename = 'F:/TITAN_BJ/Read_Titan/' + str(file[: -4]) + '.txt'
    print(filename)
    f_save = open(filename, 'w')
    f_save.write(result)
    f_save.close()
