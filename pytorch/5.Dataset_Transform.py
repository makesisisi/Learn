from torchvision import transforms
import torchvision
from torch.utils.tensorboard import SummaryWriter
import os, glob

for i in glob.glob(r"./logs/events*.*"):
    os. remove(i)

train_transform = transforms.Compose([
    transforms.ToTensor()
])

train_set = torchvision.datasets.CIFAR10(root="./4Dataset",train=True,download=True,transform=train_transform)
test_set = torchvision.datasets.CIFAR10(root="./4Dataset",train=False,download=True,transform=train_transform)

print(test_set[0])

writer = SummaryWriter("logs")

for i in range(10):
    img, target = test_set[i]
    tag = test_set.classes[target]
    writer.add_image(tag, img, i)