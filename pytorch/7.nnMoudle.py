import torch.nn as nn;
import torch.nn.functional as F

class Model(nn.modules):
    def __init__(self):
        super().__init__()
    def forward(self,x):
        x = F.relu(nn.conv2d(x));
        return F.relu(nn.conv2d(x))
    