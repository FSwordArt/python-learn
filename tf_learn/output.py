'''
sigmoid : 保证数据处在0~1之间，但不能保证所有的数据之和等于1
softmax : 能
tanh :
'''

import tensorflow as tf
'''
sigmoid
'''
# a = tf.linspace(-6., 6., 10)
# print('a:\n', a)
#
# a_sigmoid = tf.sigmoid(a)
# print('a_sigmoid:\n', a_sigmoid)
#
# x = tf.random.normal([1,28,28]) * 5
# print('x_min:\n', tf.reduce_min(x))
# print('x_max:\n', tf.reduce_max(x))
#
# x = tf.sigmoid(x)
# print('x_min:\n', tf.reduce_min(x))
# print('x_max:\n', tf.reduce_max(x))

# logits = tf.random.uniform([1, 10], minval = -2, maxval = 2)
# print('logits:\n', logits)
#
# prob = tf.nn.softmax(logits, axis=1)
# print('prob:\n', prob)
# print('prob_sum:\n', tf.reduce_sum(prob, axis=1))
