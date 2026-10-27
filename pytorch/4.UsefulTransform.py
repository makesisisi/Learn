import os, glob
from torch.utils.tensorboard import SummaryWriter
from PIL import Image
from torchvision import transforms

for i in glob.glob(r"./logs/events*.*"):
    os.remove(i)
    
img_path = r"pytorch\data\train\ants_image\0013035.jpg"
img = Image.open(img_path)

tensor_trans = transforms.ToTensor()
img_tensor = tensor_trans(img)

writer = SummaryWriter("logs")
writer.add_image("img_tensor", img_tensor)