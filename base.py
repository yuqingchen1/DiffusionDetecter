# 导入包和版本查询
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.backends.cudnn.version())
# print(torch.cuda.get_device_name(0))

'''
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision

tensor1 = torch.randn(3,4,5)     #正太随机分布数
# print(tensor)
# print(tensor.type())  # 数据类型
# print(tensor.size())  # 张量的shape，是个元组
print(tensor1.dim())   # 维度的数量

# 命名张量
# Tensor[N, C, H, W]
images = torch.randn(32, 3, 56, 56)
images.sum(dim=1)
# images.select(dim=1, index=0)

tensor2 = torch.rand(3,4,1,2)
# 使用align_to可以对维度方便地排序
# tensor = tensor.align_to('N', 'C', 'H', 'W')

from torchvision import transforms

tensor = torch.randn(3,128,128)
image = transforms.ToPILImage()(tensor)
plt.imshow(image)
plt.show()
'''

