import os, glob
from torch.utils.tensorboard import SummaryWriter
from PIL import Image
from torchvision import transforms

for i in glob.glob(r"./logs/events*.*"):
    os.remove(i)
    
writer = SummaryWriter("logs")

img_path = r"Pytorch\hymenoptera_data\train\ants\0013035.jpg"
img = Image.open(img_path)

tensor_trans = transforms.ToTensor()
img_tensor = tensor_trans(img)
writer.add_image("p",img_tensor,1)

tensor_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = tensor_norm(img_tensor)
writer.add_image("p",img_norm,2)

print(img_norm.size())
tensor_resize = transforms.Resize((512,512))
img_re = tensor_resize(img_norm)
print(img_re.size())
writer.add_image("p",img_re,3)

writer.close()