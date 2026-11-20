import shutil
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

shutil.rmtree("logs",ignore_errors=True)

transform = transforms.Compose([transforms.ToTensor()])
dataset = torchvision.datasets.CIFAR10("4Dataset",train=False,transform=transform,download=True)
dataloader = DataLoader(dataset,batch_size=64)

class Chi(nn.Module):
    def __init__(self):
        super(Chi,self).__init__()
        self.flatten = nn.Flatten()
        self.linear = nn.LazyLinear(10)
    def forward(self,x):
        x = self.flatten(x)     
        x = self.linear(x)
        return x
    
chi = Chi()


for data in dataloader:
    imgs, targets = data
    output = chi(imgs)
    print(output.shape)
