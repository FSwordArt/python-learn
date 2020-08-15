'''
where
scatter_nd
meshgrid
'''
import tensorflow as tf
import matplotlib.pyplot as plt

# a = tf.random.normal([3,3])
# print('a:\n', a)
# a_mask = a > 0
# print('a_mask:\n', a_mask)
# # a_cho = tf.boolean_mask(a, a_mask)  #挑选出为True的
# # print('a_cho:\n', a_cho)
# # a_idx = tf.where(a_mask)  #挑选为True出坐标
# # print('a_idx:\n', a_idx)
# # a_gather_nd = tf.gather_nd(a, a_idx)  #针对多维度进行提取坐标相应的元素
# # print('a_gather_nd:\n', a_gather_nd)

'''
 结合起来，有目的性的进行筛选
'''
# A = tf.ones([3,3])
# B = tf.zeros([3,3])
# C = tf.where(a_mask, A, B)
# print('C:\n', C)

'''
有目的性的更新
tf.scatter_nd(
    indices,   #将updates的数据按照indices更新到shape中
    updates,   #将要更新的数据 
    shape      #一个全是0的N维度的底板
              )
'''
##单维度
# indices = tf.constant([[4], [3], [1], [7]])
# updates = tf.constant([9, 10, 11, 12])
# shape = tf.constant([8])
#
# A = tf.scatter_nd(indices, updates, shape)
# print('A:\n', A)

##多维度
# indices = tf.constant([[0], [2]])
# updates = tf.constant([[[5,5,5,5], [6,6,6,6],
#                         [7,7,7,7], [8,8,8,8]],
#
#                        [[5,5,5,5],[6,6,6,6],
#                         [7,7,7,7], [8,8,8,8]]])
# shape = tf.constant([4,4,4])
#
# A = tf.scatter_nd(indices, updates, shape)
# print('A:\n', A)

'''
meshgrid
'''
# x = tf.linspace(-2., 2., 5)
# y = tf.linspace(-2., 2., 5)
#
# point_x, point_y = tf.meshgrid(x, y)
# print('point_x:\n', point_x)
# print('point_y:\n', point_y)
#
# points_0 = tf.stack([point_x, point_y], axis=0)
# print('points_0:\n', points_0)
#
# points_1 = tf.stack([point_x, point_y], axis=1)
# print('points_1:\n', points_1)
#
# points_2 = tf.stack([point_x, point_y], axis=2)
# print('points_2:\n', points_2)

'''
实例
'''
def func(x):
    z = tf.math.sin(x[..., 0]) + tf.math.sin(x[..., 1])
    return  z

x = tf.linspace(0., 2*3.14, 500)
y = tf.linspace(0., 2*3.14, 500)
point_x, point_y = tf.meshgrid(x, y)
points = tf.stack([point_x, point_y], axis=2)
print('points:\n', points.shape)

z = func(points)
print('z:\n',z.shape)

plt.figure('plot 2d func value')
plt.imshow(z, origin='lower', interpolation='none')
plt.colorbar()

plt.figure('plot 2d func contour')
plt.contour(point_x, point_y, z) #等高线函数
plt.colorbar()
plt.show()