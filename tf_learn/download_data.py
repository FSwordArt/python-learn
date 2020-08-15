'''
数据集加载
tf.data.Dataset
'''
import tensorflow as tf
from tensorflow.keras import datasets, layers, optimizers, Sequential, metrics
import keras
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# (x, y),(x_test, y_test) = keras.datasets.cifar10.load_data()
# print('x.shape:\n', x.shape,'\ny.shape:\n', y.shape,
#       '\nx.min:\n', x.min(), '\nx.max:\n', x.max(), '\nx.mean:\n', x.mean())
# print('x_test.shape:\n', x_test.shape, '\ny_test.shape:\n', y_test.shape)
#
# print(y[:4])
#
# y_onehot = tf.one_hot(y, depth=10)
# print('y_onehot:\n', y_onehot[:2])

'''
from_tensor_slices()
'''
# db =tf.data.Dataset.from_tensor_slices((x_test, y_test))
# db =db.shuffle(1000)#做train训练时，需要进行打乱操作
# print(next(iter(db))[0].shape)

'''
example
'''
def prepare_mnist_features_and_labels(x, y):
    x = tf.cast(x, tf.float32) / 255.0
    y = tf.cast(y, tf.int64)
    return x, y

def mnist_datset():
    (x, y), (x_val, y_val) = datasets.fashion_mnist.loda_data()
    y = tf.one_hot(y, depth=10)
    y_val = tf.one_hot(y_val, depth=10)

    ds = tf.data.Dataset.from_tensor_slices((x, y))
    ds = ds.map(prepare_mnist_features_and_labels)
    ds = ds.shuffle(1000).batch(100)

    ds_val = tf.data.Dataset.from_tensor_slices((x_val, y_val))
    ds_val = ds_val.map(prepare_mnist_features_and_labels)
    ds_val = ds_val.shuffle(1000).batch(100)

    return ds,ds_val



