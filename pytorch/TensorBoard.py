from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np
import glob, os

os.remove(glob.glob(r"../logs/events*.*"))

writer = SummaryWriter("logs")
img_path = r"pytorch\dataset\hymenoptera_data\train\ants\0013035.jpg"
image_PIL = Image.open(img_path)
image_array = np.array(image_PIL)

print(type(image_array))
print(image_array.shape)


writer.add_image("test", image_array, 1)

for i in range(100):
    writer.add_scalar("y=sin(x)", np.sin(i/10), i)
    
writer.close()