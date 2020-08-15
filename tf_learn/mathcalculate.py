import tensorflow as tf
'''
数学运算符号：
// ：表示整除
% ：表示取余
log : 以e为底
matrix-wise : [b,3,4]@[b,4,5]会生成一个[b,3,5]，进行b个相乘.和tf.matmul等价
'''
# a = tf.ones([2,2])
# b = tf.fill([2,2],2.)
# print(tf.math.log(a))
# print(tf.exp(a))
'''
实现以2或者以10为底的log
'''
# c = tf.math.log(8.)/tf.math.log(2.)
# print(c)

a = tf.ones([4,2,3])
b = tf.fill([3,5],2.)
bb = tf.broadcast_to(b,[4,3,5])
print(a@bb)


