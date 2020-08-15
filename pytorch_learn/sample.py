import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

transforms = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='D:/program_github/python/pytorch_learn/data', train=True,
                                        download=True, transform=transforms)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=0)
testset = torchvision.datasets.CIFAR10(root='D:/program_github/python/pytorch_learn/data', train=False,
                                        download=True, transform=transforms)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                          shuffle=True, num_workers=0)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# # functions to show an image
# def imshow(img):
#     img = img / 2 + 0.5     # unnormalize
#     npimg = img.numpy()
#     plt.imshow(np.transpose(npimg, (1, 2, 0)))#矩阵的转置
#     因为在plt.imshow在现实的时候输入的是（imagesize,imagesize,channels）,
#     参数img的格式为（channels,imagesize,imagesize）,
#     这两者的格式不一致，我们需要调用一次np.transpose函数
#     plt.show()
#
## some random training images
# dataiter = iter(trainloader)
# images, labels = dataiter.next()
# # show images
# imshow(torchvision.utils.make_grid(images))
# # print labels
# print(' '.join('%5s' % classes[labels[j]] for j in range(4)))
# for (input, label) in trainloader:
#     print(input.shape)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def train():
    net = Net()
    criterion = nn.CrossEntropyLoss()
    optimzer = optim.SGD(net.parameters(), lr=1e-3, momentum=0.9)

    for epoch in range(2):
        loss = 0
        for i, data in enumerate(trainloader, 0):
            inputs, label = data
            optimzer.zero_grad()
            # net.zero_grad()#和上面效果一样，但一般用上面，因为用到优化器了
            # 从0.4起, Variable 正式合并入Tensor, Variable 本来实现的自动微分功能，Tensor就能支持。读者还是可以使用Variable(tensor),
            # 但是这个操作其实什么都没做.建议读者以后直接使用tensor.要想使得Tensor使用autograd功能，只需要设置tensor.requries_grad=True.
            output = net(inputs)
            loss = criterion(output, label)
            print('反向传播之前 conv1.bias的梯度')
            print(net.conv1.bias.grad)
            loss.backward()
            print('反向传播之后 conv1.bias的梯度')
            print(net.conv1.bias.grad)
            optimzer.step()

            loss += loss.item()
            if i % 2000 == 1999:  # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, loss / 2000))

        print('Finished Training')
        path = 'D:/program_github/python/pytorch_learn/'
        #torch.save(net.state_dict(), path + 'net.pth')
        torch.save(net, path + "test.pkl")

    # Print model's state_dict
    # print("Model's state_dict:")
    # for param_tensor in net.state_dict():
    #     print(param_tensor, "\t", net.state_dict()[param_tensor].size())

    # # Print optimizer's state_dict
    # print("Optimizer's state_dict:")
    # for var_name in optimizer.state_dict():
    #     print(var_name, "\t", optimizer.state_dict()[var_name])

def test():
    model_save_path = 'D:/program_github/python/pytorch_learn/'
    model = model_save_path + "test.pkl"
    #model = model_save_path + "net.pth"
    testnet = torch.load(model)
    #model.load_state_dict(torch.load(model))

    correct = 0
    total =0
    with torch.no_grad():
        for data in testloader:
            inputs, label = data
            print("label.shape:", label.shape)
            predict = testnet(inputs)
            print("predict.shape:", predict.shape)
            _, predicted = torch.max(predict, 1)
            print("predicted.shape:", predicted.shape)
            total += label.size(0)
            correct += (predicted == label).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
            100 * correct / total))

def test_sample():
    model_save_path = 'D:/program_github/python/pytorch_learn/data'
    model = model_save_path + "test.pkl"
    testnet = torch.load(model)
    testnet.eval()

    class_correct = list(0. for i in range(10))
    class_total = list(0. for i in range(10))

    with torch.no_grad():
        for data in testloader:
            images, labels = data
            print("labels.shape:", labels.shape)
            outputs = testnet(images)
            print("outputs.shape:", outputs.shape)
            _, predicted = torch.max(outputs, 1)
            print("predicted.shape:", predicted.shape)
            c = (predicted == labels).squeeze()
            print("c.shape:", c.shape)
            print("c:", c)

            for i in range(4):
                label = labels[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1

    for i in range(10):
        print('Accuracy of %5s : %2d %%' % (
            classes[i], 100 * class_correct[i] / class_total[i]))

if __name__ == "__main__":
    train()
    test()
    #test_sample()

