from netCDF4 import *
import numpy as np
# get NC from local inputFile
nc = Dataset(inputFileName)
# 新建一个本地文件，格式是netcdf4_classic
newnc = Dataset(outputFileName, "w", format="NETCDF4_CLASSIC")


#第一部分拷贝Dimensions
# get and copy dimensions to new file
ncdimesions = nc.dimensions
# get sample_dim
if ("sample" in ncdimesions):
    sample_dim = ncdimesions["sample"]
    newncdim_sample = newnc.createDimension(sample_dim.name, sample_dim.size)
# get ddm_dim
if ("ddm" in ncdimesions):
    ddm_dim = ncdimesions["ddm"]
    newncdim_ddm = newnc.createDimension(ddm_dim.name, ddm_dim.size)
#第二部分拷贝变量的属性，维度，和数据
# !spacecraft_num!
spacecraft_num = ncvariables["spacecraft_num"]
spacecraft_num_data = spacecraft_num[:]
# copy spacecraft_num to newnc
spacecraft_num_fill_value = spacecraft_num.getncattr("_FillValue")
#新建变量，当zlib=True,fletcher32=True,chunksizes=somlist，启动压缩，默认的zlib压缩级别是4
newncspacecraft_num = newnc.createVariable(spacecraft_num.name, spacecraft_num.dtype, spacecraft_num.dimensions,                                         fill_value=spacecraft_num_fill_value, zlib=True, fletcher32=True,
                                           chunksizes=[np.uint32(1122508), ])
# 设定newncspacecraft_num的变量属性
newncspacecraft_num.long_name = "BF-1小卫星序号"
newncspacecraft_num.coordinates = spacecraft_num.getncattr("coordinates")
newncspacecraft_num.units = spacecraft_num.getncattr("units")
newncspacecraft_num.valid_range = spacecraft_num.getncattr("valid_range")
newncspacecraft_num.comment = "飞行器编号\n\t 1= BF-1A, 2 = BF-1B, 97 = 仿真器, 98 = 其他数据"
# copy spacecraft_num to newncspacecraft_num
newncspacecraft_num[:] = spacecraft_num_data
