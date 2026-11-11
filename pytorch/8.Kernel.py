import torch
import torch.nn.functional as F

input_ = torch.tensor([[1, 2, 0, 3, 1],
                       [1, 4, 5, 1, 2],
                       [1, 2, 4, 1, 2],
                       [1, 2, 4, 1, 0],
                       [0, 1, 2, 3, 4]], dtype=torch.float32)

kernel = torch.tensor([[0, 1, 2],
                       [2, 1, 3],
                       [3, 1, 0]], dtype=torch.float32)

# conv2d 要求 4 维：输入 (N, C, H, W)，卷积核 (out_c, in_c, kH, kW)
input_ = input_.reshape(1, 1, 5, 5)
kernel = kernel.reshape(1, 1, 3, 3)

output = F.conv2d(input_, kernel)

print(output)