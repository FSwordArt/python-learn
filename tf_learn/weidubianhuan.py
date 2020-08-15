import tensorflow as tf

# #不同的view
# a = tf.random.normal([4,28,28,3])
#
# pixel_num = tf.reshape(a,[4,784,3]).shape
# print(pixel_num)
#
# pixel_num_auto = tf.reshape(a,[4,-1,3]).shape#相当于b,系统会给自动计算
# print(pixel_num_auto)
#
# data_point = tf.reshape(a,[4,784*3]).shape
# print(data_point)
#
# data_point_auto = tf.reshape(a,[4,-1]).shape
# print(data_point_auto)
#
# rec_a = tf.reshape(tf.reshape(a,[4,-1]),[4,1,784,3]).shape
# print(rec_a)

# #tanspose 转置
# a = tf.random.normal([4,3,2,1])
# print(a.shape)
# print(tf.transpose(a).shape)
# print(tf.transpose(a,perm=[0,1,3,2]).shape)
# print(tf.transpose(a,[0,3,1,2]).shape)

# #增加或者减少一个维度
# a = tf.random.normal([4,35,8])
# print(tf.expand_dims(a,axis=0).shape)#正数的话会在对应位置的前面增加一个维度
# print(tf.expand_dims(a,axis=-1).shape)#负数的话会在对应位置的后面增加一个维度
# b = tf.zeros([1,2,1,3])
# print(tf.squeeze(b,axis=2).shape)
# print(tf.squeeze(b,axis=-2).shape)#去掉对应位置的维度

