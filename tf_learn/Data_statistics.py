import tensorflow as tf


'''
向量的范数
'''
# a = tf.ones([2,2])
# print(tf.norm(a))
# b = tf.ones([4, 28, 28, 3])
# print(tf.norm(b))
#
# c = tf.norm(b, ord=2, axis=1) #ord选择范数的类型，axis按某一个维度进行分割
# print(c)
'''
reduce_min/max/mean,有一个降维的作用
'''
a = tf.random.normal([4,10])
# print(tf.reduce_min(a))
# print(tf.reduce_max(a))
# print(tf.reduce_mean(a))

#从每一行中挑选某一个数进行比较，有10列，所以就有10个数
#print(tf.reduce_min(a, axis=0))

#返回最大值或者最小值所在的位置
# print(tf.argmax(a))
# print(tf.argmax(a, axis=1))

#可以利用tf.equal进行比较，然后利用tf.reduce_sum进行统计个数，计算正确率
# a = tf.constant([1,2,3,2,4])
# b = tf.range(5)
# c = tf.equal(a, b)
# print(c)
# d = tf.reduce_sum(tf.cast(c, dtype=tf.int32))
# print(d)

'''
去掉重复的部分
'''
a = tf.constant([4,2,2,4,3])
print(tf.unique(a))
#返回两个部分，一个是去掉重复以后的，另一个是和生成新的矩阵的idex的标注

