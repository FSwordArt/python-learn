'''
利用基本嵌套实现
with tf.GradientTape() as tape:
[w, grad] = tape.gradient(loss, [w])
激活函数及其梯度
loss及其梯度
crossentropy gradient
'''
import tensorflow as tf

w = tf.constant(1.)
x = tf.constant(2.)
'''
调用一次
'''
# with tf.GradientTape() as tape:
#     tape.watch([w])
#     y2 = x * w
#
# grad2 = tape.gradient(y2, [w])
# print('grad2:\n', grad2)
'''
调用多次
with tf.GradientTape(persistent=True) as tape:
'''
'''
二阶求导
'''
# w = tf.Variable(1.)
# b = tf.Variable(2.)
# x = tf.Variable(3.)
#
# with tf.GradientTape() as t1:
#     with tf.GradientTape() as t2:
#         y = x * w + b
#     dy_dw, dy_db = t2.gradient(y, [w, b])
# d2y_dw2 = t1.gradient(dy_dw, w)
#
# print(dy_dw)
# print(dy_db)
# print(d2y_dw2)
'''
激活函数及其梯度
sigmoid' = sigmoid(1 - sigmoid) 
tanh : RNN中应用较多 tanh' = 1-tanh2(x)
ReLU
'''
# a = tf.linspace(-10., 10., 10)
# print('a:\n', a)
#
# with tf.GradientTape() as tape:
#     tape.watch(a)
#     y = tf.sigmoid(a)
#     print('y:\n', y)
#
# grads = tape.gradient(y, [a])
# print('grads:\n', grads)

# print('a_relu:\n', tf.nn.relu(a))
# print('a_leaky_relu:\n', tf.nn.leaky_relu(a))#当x<0是，表达式为：kx,k是一个极小的数
'''
loss及其梯度
多输出感知机的实现
'''
# x = tf.random.normal([2,4])
# w = tf.random.normal([4,3])
# b = tf.zeros([3])
# y = tf.constant([2,0])
#
# with tf.GradientTape() as tape:
#     tape.watch([w, b])
#     prob = tf.nn.softmax(x@w + b, axis=1)
#     loss = tf.reduce_mean(tf.losses.MSE(tf.one_hot(y, depth=3), prob))
#
# grads = tape.gradient(loss, [w, b])
# print('grads:\n', grads ,
#       '\ngrads[0]:\n',grads[0],  #w
#       '\ngrads[1]:\n',grads[1])  #b
'''
crossentropy gradient
'''
# x = tf.random.normal([2,4])
# w = tf.random.normal([4,3])
# b = tf.zeros([3])
# y = tf.constant([2,0])
#
# with tf.GradientTape() as tape:
#     tape.watch([w, b])
#     logits = x@w + b
#     loss = tf.reduce_mean(tf.losses.categorical_crossentropy(tf.one_hot(y, depth=3), logits, from_logits=True))
#
# grads = tape.gradient(loss, [w, b])
# print('grads:\n', grads ,
#       '\ngrads[0]:\n',grads[0],  #w
#       '\ngrads[1]:\n',grads[1])  #b
'''
单一感知机的实现
'''
x = tf.random.normal([1,3])
w = tf.ones([3,1])
b = tf.ones([1])
y = tf.constant([1])

with tf.GradientTape() as tape:
    tape.watch([w, b])
    logits = tf.sigmoid(x@w + b)
    loss =tf.reduce_mean(tf.losses.MSE(y, logits))

grads = tape.gradient(loss, [w, b])
print('w_grads:\n', grads[0])
print('b_grads:\n', grads[1])






