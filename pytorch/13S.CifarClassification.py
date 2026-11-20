import shutil
import torch.nn as nn
import torch
from torch.utils.tensorboard import SummaryWriter

#shutil.rmtree("logs",ignore_errors=True)

class Chi(nn.Module):
    def __init__(self):
        super(Chi,self).__init__()
        '''self.conv1 = nn.Conv2d(3,32,5,padding=2)
        self.pool1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(32,32,5,padding=2)
        self.pool2 = nn.MaxPool2d(2)
        self.conv3 = nn.Conv2d(32,64,5,padding=2)
        self.pool3 = nn.MaxPool2d(2)
        self.flatten = nn.Flatten()
        self.Linear1 = nn.LazyLinear(64)
        self.Linear2 = nn.LazyLinear(10)
        self.softmax = nn.Softmax()'''
        
        self.model1 = nn.Sequential(
            nn.Conv2d(3,32,5,padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,32,5,padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,64,5,padding=2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.LazyLinear(64),
            nn.Linear(64, 10)
        )
        
    def forward(self,x):
        x = self.model1(x)
        return x
    
chi = Chi()
input = torch.ones((64,3,32,32))
output = chi(input)
print(output.shape)

writer =SummaryWriter("logs_seq")
writer.add_graph(chi,input)
writer.close()
        