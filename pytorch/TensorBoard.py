from torch.utils.tensorboard import SummaryWriter
import numpy as np

writer = SummaryWriter("logs")

#writer.add_image

for i in range(100):
    writer.add_scalar("y=sin(x)", np.sin(i/10), i)
    
writer.close()