import struct
import numpy as np
import os


data = np.fromfile('F:/CI_V3/CI/20150704_CI.b', dtype=np.int32)
data = np.reshape(data, (-1, 270, 350))
print(np.shape(data))

np.savetxt('F:/CI_result/save/label1.txt', data[:, :, :], fmt='%1.0f')

# r_f = os.listdir('F:/CI_V3/CI')
# domain = os.path.abspath('F:/CI_V3/CI') #获取文件夹的路径，此处其实没必要这么写，目的是为了熟悉os的文件夹操作
# # nx = 270
# # ny = 350
# for info in os.listdir('F:/CI_V3/CI'):
#     info = os.path.join(domain,info) #将路径与文件名结合起来就是每个文件的完整路径
#     data = np.fromfile(info, dtype = np.int32)
#     # print(data)
#     print(np.shape(data))
#     with open(data, 'rb') as f:
#         print(np.shape(f))
#         f = np.reshape(f, (-1, 270, 350))
#         print(np.shape(f))
# #     info = np.reshape(info, (-1, 270, 350))
# #     (nz, nx, ny) = np.shape(info)
# #     print("nz = ", nz)
# #     print("nx = ", nx)
# #     print("ny = ", ny)