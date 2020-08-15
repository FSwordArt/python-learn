import tensorflow as tf
import numpy as np


# print(tf.constant([True,False]))
# print(tf.constant('hello,tensorflow'))

# a = np.array(5)
# print(a.dtype)
#
# aa = tf.convert_to_tensor(a)
# print(aa)
# #使用tf.cast进行数据类型的转换
# aaa = tf.cast(aa, dtype = tf.float64)
# print(aaa)

# a = tf.convert_to_tensor(np.ones([2,3]))
# print(a)

# a = tf.zeros([2,3,3])
# print(tf.zeros_like(a))

# #填充为一个2*2的全是1的矩阵
# a = tf.fill([2,2],1)
# print(a)

# #随机初始化--正态分布
# a = tf.random.normal([2,2],mean = 0,stddev = 1)
# print(a)
# #truncate 截断的正态分布,在标准正态分布，截去某一部分
# b = tf.random.truncated_normal([2,2],mean = 0,stddev = 1)
# print(b)

# #随机初始化--均匀分布
# a = tf.random.uniform([2,2], minval=0, maxval=1)
# print(a)

# #随机打散
# idx = tf.range(10)
# idx = tf.random.shuffle(idx)
# print(idx)
#
# a = tf.random.normal([10,784])
# b = tf.random.uniform([10],maxval = 10,dtype=tf.int32)
# print(a)
# print(b)
#
# # a = tf.gather(a,idx)
# b = tf.gather(b,idx)
# print(a)
# print(b)

# out = tf.random.uniform([4,10])
# y = tf.range(4)
# y = tf.one_hot(y,depth = 10)
# print(y)
#
# loss = tf.keras.losses.mse(y,out)
# print(loss)
#
# loss = tf.reduce_mean(loss)
# print(loss)

# #切片
# #:的作用
# a = tf.random.normal([4,28,28,3])
# print(a[1].shape)
# print(a[1,2].shape)#与a[1][2].shape一样
# print(a[1,2,3].shape)
# print(a[1,2,3,2].shape)#B通道
# print(a[0,:,:,:].shape)
# print(a[:,:,:,0].shape)
# print(a[0:2,0:28:2,12:,:])

# #。。。的作用
# a = tf.random.normal([2,4,28,28,3])
# print(a[0,...].shape)#相当于a[0,:,:,:,:]
# print(a[...,0].shape)
# print(a[1,0,...,0,:].shape)

# #tf.gather()的用法：用一个一维的索引数组，将张量中对应索引的向量提取出来
# a = tf.Variable([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# index_a = tf.Variable([0,2])
# b = tf.Variable([1,2,3,4,5,6,7,8,9,10])
# index_b = tf.Variable([2,4,6,8])
# print(tf.gather(a, index_a))
# print(tf.gather(b, index_b))

# #tf.gather_nd的用法
# #假设 a.shape = [4,35,8]
# #input:tf.gather_nd(a,[0]).shape
# #output: [35,8]
#
# #input:tf.gather_nd(a,[0,1]).shape
# #output: [8]
#
# #input:tf.gather_nd(a,[0,1,2]).shape
# #output: []返回一个课程的成绩
#
# #input:tf.gather_nd(a,[[0,1,2]]).shape
# #output: [1]#返回一个课程的成绩，为一个一维数组

## tf.boolean_mask的用法 维度要和比较的维度相同
# a = tf.ones([2,3,4])
# print(a)
# b = tf.boolean_mask(a,mask=[[True,False,False],[False,True,True]])
# print(b)


