import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets
import os

#屏蔽一些tf无用的信息
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#x:[60k,28,28]
#y:[60k]
(x,y),_ = datasets.mnist.load_data()

#创建一个tensor，x:[0-255] => [0-1.]
x = tf.convert_to_tensor(x, dtype = tf.float32) / 255
y = tf.convert_to_tensor(y, dtype = tf.int32)

#查看x,y的维度以及类型
print(x.shape, y.shape, x.dtype, y.dtype)

#查看x,y的最小值和最大值
print(tf.reduce_min(x), tf.reduce_max(x))
print(tf.reduce_min(y), tf.reduce_max(y))

#取128作为一个batch
train_db = tf.data.Dataset.from_tensor_slices((x,y)).batch(128)
train_iter = iter(train_db)
sample = next(train_iter)
print('batch:',sample[0].shape,sample[1].shape)

#降维步骤：[b,784] => [b,256] => [b,128] => [b,10]
#w的维度：[dim_in,dim_out], b的维度：[dim_out]
w1 = tf.Variable(tf.random.truncated_normal([784, 256]))
b1 = tf.Variable(tf.zeros([256]))
w2 = tf.Variable(tf.random.truncated_normal([256, 128]))
b2 = tf.Variable(tf.zeros([128]))
w3 = tf.Variable(tf.random.truncated_normal([128, 10]))
b3 = tf.Variable(tf.zeros([10]))
lr = 1e-3
for step, (x, y) in enumerate(train_db):
    #x:[128,28,28]
    #y:[128]
    
    #x:[b,28,28] => [b,28*28]
    x = tf.reshape(x,[-1,28*28])
    
    with tf.GradientTape() as tape:
        #x:[b,28*28]
        #h1 = x@w1 + b1
        #[b,784]@[784,256] + [256] => [b,256] + [256] => [b,256] + [b,256]
        h1 = x@w1 + b1#h1 = x@w1 + tf.broadcast_to(b, [x.shape[0],256])
        h1 = tf.nn.relu(h1)      
        #[b,256] => [b,128]
        h2 = h1@w2 + b2
        h2 = tf.nn.relu(h2)        
        #[b,128] => [b,10]
        out = h2@w3 + b3
        
        #compute loss
        #out:[b,10]
        #y:[b]
        y_onehot = tf.one_hot(y, depth=10)        
        #mse = mean(sum(y-out)**2)
        #shape:[b,10]
        loss = tf.square(y_onehot - out)        
        #mean:scalar
        loss = tf.reduce_mean(loss)
    
    #compute gradients
    grads = tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
    w1 = w1 - lr * grads[0]
    b1 = b1 - lr * grads[1]
    w2 = w2 - lr * grads[2]            
    b2 = b2 - lr * grads[3]
    w3 = w3 - lr * grads[4]
    b3 = b3 - lr * grads[5]
    
    if step % 100 ==0:
        print(step, 'loss', float(loss))