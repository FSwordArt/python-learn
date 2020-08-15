import tensorflow as tf
'''
Broadcasting:张量维度扩张的手段，对某一个维度重复N多次，但没有真正的复制数据，
与tf.tile相反，这个会真正的复制N次的数据。
可以认为Broadcasting是数据优化的手段，没有真正的复制数据，但可以表现为数据扩张了
优势：方便书写，内存节省
'''
x = tf.random.normal([4,32,32,3])
print((x + tf.random.normal([3])).shape)
print((x + tf.random.normal([32,32,1])).shape)
print((x + tf.random.normal([1,1,1,1])).shape)
#print((x + tf.random.normal([1,4,1,1])).shape)#会失败，因为第二个4不是1，无法进行
b = tf.broadcast_to(tf.random.normal([4,1,1,1]),[4,32,32,3])
print(b.shape)

a = tf.ones([3,4])
a1 = tf.broadcast_to(a,[2,3,4])
print(a1,'\n',a1.shape)
a2 = tf.expand_dims(a,axis=0)
print(a2)
a3 = tf.tile(a2,[2,1,1])
print(a3,'\n',a3.shape)






