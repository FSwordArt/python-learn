'''
keras.Sequential([layer1, layer2, layer3])
每一个layers喂一个Dense
'''
import tensorflow as tf
from tensorflow import keras
# x = tf.random.normal([4,784])
# net = tf.keras.layers.Dense(512)
# out = net(x)
# print(out.shape)
# print(net.kernel.shape, net.bias.shape)

x = tf.random.normal([2, 3])
model = keras.Sequential([
        keras.layers.Dense(2, activation='relu'),
        keras.layers.Dense(2, activation='relu'),
        keras.layers.Dense(2)
    ])

model.build(input_shape=[None, 3])
model.summary() #相当于print

for p in model.trainable_variables:
    print(p.name, p.shape)






