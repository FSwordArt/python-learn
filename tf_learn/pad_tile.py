'''
pad : 数据的填充
tile : 数据的复制,与broadcast_to相比，后者的性能更为强大，占用较少的内存

'''
import tensorflow as tf

a = tf.reshape(tf.range(9), [3,3])
print('a:\n', a)
# b = tf.pad(a,[[0,0],[0,0]])#第一个矩阵代表行，第二个代表列
# print('b:\n', b)
# c = tf.pad(a,[[1,0],[0,0]])
# print('c:\n', c)
# d = tf.random.normal([4,28,28,3])
# d1 = tf.pad(d,[[0,0], [2,2], [2,2], [0,0]])
# print('d1_shaped:\n', d1.shape)

# a_tile_1 = tf.tile(a, [2,1]) #2代表行复制一倍，1代表不复制
# print('a_tile_1:\n', a_tile_1)
# a_tile_2 = tf.tile(a, [1,2])
# print('a_tile_2:\n', a_tile_2)

aa = tf.expand_dims(a,axis=0)
print('aa:\n', aa)
aaa = tf.tile(aa, [2,1,1])
print('aaa:\n', aaa)
a_broadcast = tf.broadcast_to(aa, [2,3,3])
print('a_broadcast:\n', a_broadcast)