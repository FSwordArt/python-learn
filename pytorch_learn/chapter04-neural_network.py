# -*- coding: utf-8 -*
# 优化方法的基本使用方法
# 如何对模型的不同部分设置不同的学习率
# 如何调整学习率

import numpy as np
import torch
import torch.nn as nn
from torch import  optim

# 首先定义一个LeNet网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.features = nn.Sequential(

                    nn.Conv2d(3, 6, 5),
                    nn.ReLU(),
                    nn.MaxPool2d(2,2),
                    nn.Conv2d(6, 16, 5),
                    nn.ReLU(),
                    nn.MaxPool2d(2,2)
        )

        self.classifier = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(-1, 16 * 5 * 5)
        x = self.classifier(x)
        return x

net = Net()


optimizer = optim.SGD(params=net.parameters(), lr=1)
optimizer.zero_grad() # 梯度清零，等价于net.zero_grad()

input = torch.randn(1, 3, 32, 32)
output = net(input)
output.backward(output) # fake backward

optimizer.step() # 执行优化

# # 为不同子网络设置不同的学习率，在finetune中经常用到
# # 如果对某个参数不指定学习率，就使用最外层的默认学习率
# optimizer =optim.SGD([
#                 {'params': net.features.parameters()}, # 学习率为1e-5
#                 {'params': net.classifier.parameters(), 'lr': 1e-2}
#             ], lr=1e-5)
#
# print(optimizer)

# # 只为两个全连接层设置较大的学习率，其余层的学习率较小
# special_layers = nn.ModuleList([net.classifier[0], net.classifier[3]])
# special_layers_params = list(map(id, special_layers.parameters()))
# print(special_layers_params)
#
# base_params = filter(lambda p: id(p) not in special_layers_params,
#                      net.parameters())
# print(base_params)
#
# optimizer = torch.optim.SGD([
#             {'params': base_params},
#             {'params': special_layers.parameters(), 'lr': 0.01}
#         ], lr=0.001 )
#

# print(optimizer)
# print("end")

'''初始化'''
'''
# 利用nn.init初始化
from torch.nn import init
linear = nn.Linear(3, 4)

torch.manual_seed(1)
# 等价于 linear.weight.data.normal_(0, std)
init.xavier_normal_(linear.weight)


# 直接初始化
import math
torch.manual_seed(1)

# xavier初始化的计算公式
std = math.sqrt(2)/math.sqrt(7.)
linear.weight.data.normal_(0,std)
'''
'''
# 在PyTorch中保存模型十分简单，所有的Module对象都具有state_dict()函数，
# 返回当前Module所有的状态数据。将这些状态数据保存后，下次使用模型时即可利用model.load_state_dict()函数将状态加载进来。
# 优化器（optimizer）也有类似的机制，不过一般并不需要保存优化器的运行状态
# 保存模型
t.save(net.state_dict(), 'net.pth')

# 加载已保存的模型
net2 = Net()
net2.load_state_dict(t.load('net.pth'))
'''

'''
至于如何在多个GPU上并行计算，PyTorch也提供了两个函数，可实现简单高效的并行GPU计算

nn.parallel.data_parallel(module, inputs, device_ids=None, output_device=None, dim=0, module_kwargs=None)
class torch.nn.DataParallel(module, device_ids=None, output_device=None, dim=0)

可见二者的参数十分相似，通过device_ids参数可以指定在哪些GPU上进行优化，output_device指定输出到哪个GPU上。
唯一的不同就在于前者直接利用多GPU并行计算得出结果，而后者则返回一个新的module，能够自动在多GPU上进行并行加速。

# method 1
new_net = nn.DataParallel(net, device_ids=[0, 1])
output = new_net(input)

# method 2
output = nn.parallel.data_parallel(new_net, input, device_ids=[0, 1])
'''
'''
Resnet 34 网络结构
'''

