# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# #####Session会话控制#####
# matrix1 = tf.constant([[3,3]])
# matrix2 = tf.constant([[2],
#                        [2]])
#
# product = tf.matmul(matrix1,matrix2) #matrix multiply np.dot(m1,m2)
#
# ###method 1
# #sess = tf.Session()
# #result = sess.run(product)
# #print(result)
# #sess.close()
#
#
# ###method 2
# with tf.Session() as sess:
#     print(sess.run(product))



# #####Variable变量#####
# state = tf.Variable(0,name = 'counter')
# print(state)
# one = tf.constant(1)
#
# new_value = tf.add(state,one)
# update = tf.assign(state,new_value)
#
# init = tf.initialize_all_variables()  #激活变量必须
#
# with tf.Session() as sess:
#     sess.run(init)
#     for _ in range(3):
#         sess.run(update)
#         print(sess.run(state))



# #####placehold传入值#####
# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
#
# output = tf.multiply(input1,input2)
#
# with tf.Session() as sess:
#     print(sess.run(output,feed_dict = {input1:7.,input2:2.}))
#


#####添加层def add_layer#####
def add_layers(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random.normal([in_size, out_size]), name='W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)

        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


#####build a neural network#####
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]  # 相当于[:,done]展成列向量
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# add hidden layer
l1 = add_layers(xs, 1, 10, activation_function=tf.nn.relu)
# add output layer
prediction = add_layers(l1, 10, 1, activation_function=None)
# the error between prediction and real data
with tf.name_scope('lose'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                        reduction_indices=[1]))
# reduction_indices = [1],按行求和；reduction_indices = [0],按列求和
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
writer = tf.summary.FileWriter("logs/", sess.graph)
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()
# plt.show()
for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # print(sess.run(loss,feed_dict = {xs:x_data,ys:y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)































