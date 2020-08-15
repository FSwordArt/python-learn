import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, optimizers, Sequential, metrics


(x, y), (x_test, y_test) = datasets.fashion_mnist.load_data()
print(x.shape, y.shape)

# db = tf.data.Dataset.from_tensor_slices((x, y ))
# db = db.map()








def main():
    pass










if __name__ == '__main__':
    main()