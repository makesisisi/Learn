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
dataloader = DataLoader(dataset,batch_size=64,)

class Chi(nn.Module):
    def __init__(self):
        super(Chi,self).__init__()
        self.conv2d = nn.Conv2d(in_channels=3,out_channels=6,kernel_size=3,stride=1,padding=0)
        
    def forward(self,x):
        x = self.conv2d(x)
        return x
    
chi = Chi()    

writer = SummaryWriter("logs")

step = 0
for data in dataloader:
    imgs, tagets = data
    output = chi(imgs)
    writer.add_images("input",imgs,step)
    imgs = torch.reshape(output,(-1,3,30,30))
    writer.add_images("output",imgs,step)
    step += 1
    

    