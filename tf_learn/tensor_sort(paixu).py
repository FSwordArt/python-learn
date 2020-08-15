'''
Sort : 排序
argsort : 获得位置，index
Topk :
Top-5 Acc :
'''
import tensorflow as tf

# a = tf.random.uniform([3,3], maxval=10, dtype=tf.int32)
# print('a: \n'+ str(a))
# aa = tf.sort(a)
# print('aa: \n' + str(aa))
# aaa = tf.sort(a, direction='DESCENDING')
# print('aaa: \n'+ str(aaa))
# idx = tf.argsort(a)
# print('idx: \n'+ str(idx))

'''
Top_k
'''
# a = tf.random.uniform([3,3], maxval=10, dtype=tf.int32)
# print('a:\n' + str(a))
# res = tf.math.top_k(a, 2)
# print('res:\n' + str(res))
# print('res0:\n' + str(res.indices))#相当于argsort
# print('res1\n' + str(res.values))#相当于sort
'''
Top-k accuracy
'''
# prob = tf.constant([[0.1, 0.2, 0.7], [0.2, 0.7, 0.1]])
# target = tf.constant([2, 0])
# k_b = tf.math.top_k(prob, 3).indices
# print('k_b:\n' + str(k_b))
# k_b1 = tf.transpose(k_b, [1,0])
# print('k_b1:\n' + str(k_b1))
# target1 = tf.broadcast_to(target, [3,2])
# print('target1:\n' + str(target1))

