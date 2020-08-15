# -*- coding: utf-8 -*
'''
DataLoader的函数定义如下： DataLoader(dataset, batch_size=1, shuffle=False,
sampler=None, num_workers=0, collate_fn=default_collate, pin_memory=False, drop_last=False)

dataset：加载的数据集(Dataset对象)
batch_size：batch size
shuffle:：是否将数据打乱
sampler： 样本抽样，后续会详细介绍
num_workers：使用多进程加载的进程数，0代表不使用多进程
collate_fn： 如何将多个样本数据拼接成一个batch，一般使用默认的拼接方式即可
pin_memory：是否将数据保存在pin memory区，pin memory中的数据转到GPU会快一些
drop_last：dataset中的数据个数可能不是batch_size的整数倍，drop_last为True会将多出来不足一个batch的数据丢弃
'''

'''
dataloader是一个可迭代的对象，意味着我们可以像使用迭代器一样使用它，例如：

for batch_datas, batch_labels in dataloader:
    train()
或

dataiter = iter(dataloader)
batch_datas, batch_labesl = next(dataiter)
'''

