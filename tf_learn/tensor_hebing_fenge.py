'''
tf.concat : 拼接，axis的维度可以不等，别的必须相同
tf.spit :  分割
tf.stack : 堆叠,创造了一个新的维度，所有的维度必须相等
tf.unstack : 分割
'''
import  tensorflow as tf

#拼接一个数据
a = tf.ones([4, 35, 8])
b = tf.ones([4, 35, 8])
c = tf.concat([a,b], axis=0)
d = tf.stack([a,b], axis=0)
print(c.shape)
print(d.shape)

#分割一个数据
e, f = tf.unstack(d, axis=0)
print(e.shape, f.shape)

res = tf.unstack(d, axis=3)
print(res[0].shape, res[4].shape)
print(len(res))

res = tf.split(d, axis=3, num_or_size_splits=2)
print(len(res))
res = tf.split(d, axis=3, num_or_size_splits=[2, 2, 4])
print(res[0].shape, res[1].shape, res[2].shape)


