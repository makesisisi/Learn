from torch.utils.data import Dataset  #导入pytorch中用来读取数据集的模块
from PIL import Image  #导入PIL库中的Image模块，用于图像的读取和处理
import os #导入os模块，用于操作文件和目录
class MyData(Dataset):   #自定义数据集类，继承自torch.utils.data.Dataset
    def __init__(self, root_dir, label_dir): 
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)  #获取指定路径下的所有文件名，并将其存储在self.img_path中，以便在__getitem__方法中使用。

    def __getitem__(self, idx):
        img_name = self.img_path[idx] 
        img_item_path = os.path.join(self.root_dir,self.label_dir,img_name)
        img=Image.open(img_item_path)
        label = self.label_dir 
        return img, label  
    
    def __len__(self):
        return len(self.img_path)   #用于返回数据集的大小，即数据集中样本的数量。