import torchvision
from torchvision import transforms
import shutil
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader

shutil.rmtree("logs", ignore_errors=True)

test_set = torchvision.datasets.CIFAR10("4Dataset",transform=transforms.ToTensor(),train=False)

test_loader = DataLoader(dataset=test_set,batch_size=4,shuffle=True, num_workers=0,drop_last=False)

writer = SummaryWriter("logs")

for i, (img, target) in enumerate(test_loader):
    writer.add_images("test_data",img,i)
    if i > 10 : break

print('Done')