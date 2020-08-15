import numpy as np
import torch

# x = torch.randn(5, 3)
# print("x:", x)
# y = torch.randn(5, 3)
# print("y:", y)
# result = torch.Tensor(5, 3)
# torch.add(x, y, out=result)
# print("result:", result)

# a = np.ones(5)
# b = torch.from_numpy(a)
# c = b.add_(1)
#
# #获取某个元素值，使用scalar.item。直接tensor[index]得到的还是一个Tensor，一个0—dim的tensor,一般称为scalar
# scalar = b[0]
# print(scalar)
# print(scalar.item())
# d = torch.tensor([2])
# print(d)
# print(d.item())

# a = torch.Tensor([[1,2,3],[4,5,6]])
# print(a)
# print(a.size())
# b = a.tolist()
# print(b)
# print(a.numel())

# a = torch.arange(0,10,2)
# print(a)
# b = torch.range(0,10,2)
# print(b)

# a = torch.arange(0, 16).view(4, 4)
# print(a)
# index = torch.LongTensor([[0,1,2,3],[3,2,1,0]]).t()
# print(index)
# b = a.gather(1, index)
# print(b)
#
# c = torch.zeros(4,4)
# c.scatter_(1, index, b.float())
# print(c)

a = torch.arange(0, 6)
# print(a)
# print(a.storage())

a[1] = 100
# print(a)

c = a[2:]
print(c)
print(c.storage())

print(c.data_ptr(), a.data_ptr())

