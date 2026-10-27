from torchvision import transforms
from PIL import Image
from torch.utils.tensorboard import SummaryWriter
import os, glob
import cv2

for i in glob.glob(r"./logs/events*.*"):
    os.remove(i)

img_path = r"pytorch\data\train\ants_image\0013035.jpg"
img = Image.open(img_path)
tensor_trans = transforms.ToTensor()
img_tensor = tensor_trans(img)

writer = SummaryWriter("logs")
writer.add_image("Tensor_img",img_tensor)

print(type(img_tensor))
