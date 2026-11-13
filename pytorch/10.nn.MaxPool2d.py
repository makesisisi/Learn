import shutil

import torch
import torch.nn as nn

import torchvision
import torchvision.transforms as transforms

from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

shutil.rmtree("logs",ignore_errors=True)

transform = transforms.Compose([transforms.ToTensor()])
dataset = torchvision.datasets.CIFAR10("4Dataset",train=False,transform=transform,download=True)
dataloader = DataLoader(dataset,batch_size=64)

class Chi(nn.Module):
    def __init__(self):
        super(Chi,self).__init__()
        self.MaxPool2d = nn.MaxPool2d(kernel_size=3,ceil_mode=True)
        
    def forward(self,x):
        x = self.MaxPool2d(x)
        return x
    
chi = Chi()
    
writer = SummaryWriter("logs")
    
step = 0
for data in dataloader:
    imgs, targets = data
    output = chi(imgs)
    writer.add_images("input",imgs,step)
    writer.add_images("output",output,step)
    step += 1

writer.close()

#池化的作用就是在保留特征的同时尽量减小数据量