'''
loss
交叉熵
'''
import tensorflow as tf

# y = tf.constant([1,2,3,0,2])
# y = tf.one_hot(y, depth=4)
# y = tf.cast(y, dtype=tf.float32)
#
# out = tf.random.normal([5,4])
#
# loss1 = tf.reduce_mean(tf.square(y-out))
# loss2 = tf.reduce_sum(tf.square(y - out)) / (5*4)
# loss3 = tf.square(tf.norm(y - out)) / (5*4)
# loss4 = tf.reduce_mean(tf.losses.MSE(y, out))#VS MeanSquaredError is a class
#
# print('loss1:\n', loss1)
# print('loss2:\n', loss2)
# print('loss3:\n', loss3)
# print('loss4:\n', loss4)
'''
Categorical cross entropy 交叉熵
'''
# a = tf.losses.categorical_crossentropy([0,1,0,0],[0.25,0.25,0.25,0.25])
# print('a:\n', a)
# b = tf.losses.categorical_crossentropy([0,1,0,0],[0.1,0.1,0.8,0.1])
# print('b:\n', b)
# c = tf.losses.categorical_crossentropy([0,1,0,0],[0.1,0.7,0.1,0.1])
# print('c:\n', c)
# d = tf.losses.categorical_crossentropy([0,1,0,0],[0.01,0.97,0.01,0.01])
# print('d:\n', d)
# e = tf.losses.binary_crossentropy([1],[0.1])
# print(e)
'''
为什么不用sigmoid + MSE : gradient vanish 梯度消失现象

'''
x = tf.random.normal([1,784])
w = tf.random.normal([784,2])
b = tf.zeros([2])

logits = x@w + b
print('logits:\n', logits)

prob = tf.math.softmax(logits, axis=1)
print('prob:\n', prob)

prob_cross_entropy = tf.losses.categorical_crossentropy([0,1], logits, from_logits=True)
print('prob_cross_entropy:\n', prob_cross_entropy)
