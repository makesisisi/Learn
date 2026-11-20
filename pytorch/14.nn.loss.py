import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("4Dataset",train=False,transform=transforms.ToTensor())
dataloader = DataLoader(dataset,64)

'''
inputs = torch.tensor([1,2,3],dtype=torch.float32)
targets = torch.tensor([1,2,5],dtype=torch.float32)

torch.reshape(inputs,(1,1,1,3))
torch.reshape(targets,(1,1,1,3))

loss1 = nn.L1Loss()
loss2 = nn.MSELoss()
loss3 = nn.CrossEntropyLoss()
result1 = loss1(inputs, targets)
result2 = loss2(inputs, targets)
result3 = loss3(inputs, targets)
print(result1,result2,result3)
'''

class Chi(nn.Module):
    def __init__(self):
        super(Chi,self).__init__()
        
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
loss = nn.CrossEntropyLoss()

for data in dataloader:
    imgs, targets = data
    output = chi(imgs)
    result_loss = loss(output,targets)
    result_loss.backward()