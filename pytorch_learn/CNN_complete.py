import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim import lr_scheduler
from torch.utils.data import DataLoader

class CNet(nn.Module):
    def __init__(self, inputs, outputs, kernel_size = 5):
        super(CNet, self).__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(inputs, outputs, kernel_size=kernel_size),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
        )

    def forward(self, x):
        return self.conv(x)

class FCNet(nn.Module):
    def __init__(self, inputs, outputs):
        super(FCNet, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(inputs, outputs),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.fc(x)

class UseNet(nn.Module):
    def __init__(self):
        super(UseNet, self).__init__()

        self.conv1 = CNet(3, 6)
        self.conv2 = CNet(6, 16)

        self.fc1 = FCNet(16*5*5, 120)
        self.fc2 = FCNet(120, 84)
        self.fc3 = FCNet(84, 10)

    def forward(self, x):
        _, _, H, W = x.shape

        c1 = self.conv1(x)
        c2 = self.conv2(c1)

        c2 = c2.view(-1, 16*5*5)

        f1 = self.fc1(c2)
        f2 = self.fc2(f1)
        f3 = self.fc3(f2)

        return f3

transforms = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='D:/program_github/python/pytorch_learn/data', train=True,
                                        download=True, transform=transforms)
trainloader = DataLoader(trainset, batch_size=4,
                         shuffle=True, num_workers=0)

testset = torchvision.datasets.CIFAR10(root='D:/program_github/python/pytorch_learn/data', train=False,
                                       download=True, transform=transforms)
testloader = DataLoader(testset, batch_size=4,
                        shuffle=True, num_workers=0)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

model_save_path = "D:/program_github/python/pytorch_learn/"

def train():

    net = UseNet()
    net.train()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr = 1e-3, momentum = 0.9)
    scheduler = lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.3)

    for epoch in range(2):
        loss = 0
        for i, data in enumerate(trainloader, 0):
            inputs, label = data
            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, label)
            loss.backward()
            optimizer.step()

            loss += loss.item()
            if i % 2000 == 1999: # print every 2000 mini-batches
                print("[%d, %5d] loss: %.3f" %
                      (epoch + 1, i + 1, loss / 2000))

        scheduler.step()

    print("Finished Training")
    torch.save(net, model_save_path + "test.pkl")

def test():
    model = model_save_path + "test.pkl"
    testnet = torch.load(model)
    testnet.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for data in testloader:
            inputs, label = data

            predict = testnet(inputs)
            # print("prediact.shape:", predict.shape)
            _, predicted = torch.max(predict, 1)
            # print("predicted.shape:", predicted.shape)

            total += label.size(0)
            correct += (predicted == label).sum().item()

    print("Accuracy of the network on the 10000 test images: %d %%" %(
            100 * correct / total))

if __name__ == "__main__":
    #train()
    test()






