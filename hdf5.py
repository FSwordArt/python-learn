

import h5py  # 导入工具包
import numpy as np

# HDF5的写入：
imgData = ["a".encode("ascii"),"b".encode("ascii"),"c".encode("ascii")]
with h5py.File("file.h5", 'w') as f:
    f['data'] = imgData  # 将数据写入文件的主键data下面
    f['labels'] = range(3)  # 将数据写入文件的主键labels下面


# # 读 h5 文件里面的数据
# with h5py.File('xxx.h5', 'r') as f:
# 	for key in f.keys()
# 		print(f[key].name)
# 		print(f[key].value)
#

# HDF5的读取：
f = h5py.File('file.h5', 'r')  # 打开h5文件
print(f)
  # 可以查看所有的主键
print(f.keys())
a = f['data'][:]  # 取出主键为data的所有的键值
b = f['labels'][:]
print(a.decoder())
print(b)
f.close()

# with h5py.File('file.h5', 'r') as f:
#     for item in f.keys():
#         print('main key is: {}'.format(item))
#         content = f[item][:]
#         print('key value of {0} is: {1}'.format(item,content))
# f.close()