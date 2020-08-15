import torch
import numpy as np
#
# x = torch.empty(5,3)
# print(x)
#
# x = torch.rand(1)
# print(x)
# print(x.item())
#
# a = np.ones(5)
# b = torch.from_numpy(a)
# np.add(a, 1, out = a)
# print(a) # 如果a 变的话， b也会跟着变，说明b只是保存了一个地址而已，并没有深拷贝
# print(b)
#
# a = np.ones(5)
# b = torch.from_numpy(a)# ndarray --> Tensor
# a_ = b.numpy() # Tensor --> ndarray
# np.add(a_, 1, out=a_) # 会影响 b 的值
# print(a)
# print(b)

# a = ["a", "b", "c", "d"]
# for i,k in enumerate(a, 10):
#     print(i)
#     print(k)
#     print("----------------------------")


# a = list(0. for i in range(10))
# print(a)

a = np.unique([1,2,3,4,1,6,8])
print(a)
b = a[1:]
print(b)





