'''
clip_by_value :
clip_by_norm :
gradient clipping :
'''
import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, optimizers, Sequential, metrics
import os
'''
clip_by_value
'''
#a = np.arange(10)
# a = tf.convert_to_tensor(a)
# print('a:\n',a)
# aa = tf.maximum(a, 2)  #当a的值小于2时，取其为2
# print('aa:\n',a)
# aaa = tf.minimum(a, 8)#当a的值大于8时，取其为8
# print('aaa:\n',aaa)
# aaaa = tf.clip_by_value(a, 2, 8) #为上面两个的结合体
# print('aaaa:\n',aaaa)
# a1 = a - 5
# a2 = tf.nn.relu(a1)
# print('a2:\n', a2)
# a3 = tf.maximum(a1,0)
# print('a3:\n', a3)
'''
clip_by_norm
'''
# a = tf.random.normal([2,2], mean=10)
# print('a:\n', a)
# a1 = tf.norm(a) #二范数
# print('a1:\n', a1)
# a2 = tf.clip_by_norm(a,15) #保持梯度的方向不变而进行限幅，将其二范数修正为所要的数
# print('a2:\n', a2)
# a3 = tf.norm(a2)
# print('a3:\n', a3)
'''
gradient clipping,
对于神经网络，含有多个参数，一般采用new_grads,total_norm=tf.clip_by_global_norm(grads,25)
clip_by_global_norm j发生gradient exploding，进行等比例裁剪
保持方向不变
'''


