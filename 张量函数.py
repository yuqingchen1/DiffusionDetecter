
import PIL
import torch
import torchvision
from matplotlib import pyplot as plt
from torchvision import transforms

'''
a = torch.randn(2, 3, 4)        # Tensor[N, C, H, W]   # N：Batch，批处理大小
print(a)
print(a.size())
print(a.dim())
# image = transforms.ToPILImage()(a)
# plt.imshow(image)
# plt.show()
'''

# 返回与 input 大小相同的张量
# noise = torch.randn_like(a)

'''
# transforms.ToPILImage()(a)   将张量a转换成图片
image = transforms.ToPILImage()(a)
print(a)
print(a.shape)
plt.imshow(image)
plt.show()

# 将图片转换成张量b
b = transforms.ToTensor()(image)
print(b)

# 将tensor转换为numpy       # numpy[N, H, W, C]
b = a.numpy()
print(b)

# 将numpy转换成tensor
c = torch.from_numpy(b)
print(c)
'''

'''
# 张量的拆分和拼接
# dim=0是按照行拆分，dim=1是按照列拆分, dim=2在矩阵的方向上划分
b = torch.split(a, 1, dim=0)    # 按块大小拆分张量, 第二个数字代表每一块在该维度的尺寸大小
print(b)

c = torch.chunk(a, 2, dim=0)    # 第二个数字代表要拆成多少块

d = torch.cat((a, a), dim=0)     # 按已有维度拼接张量

e = torch.stack((a, a), dim=0)      # 沿着一个新维度对输入张量序列进行连接

# 将整数标签转为one-hot编码
num_class = 5                      # 类别数
N = 3
tensor = torch.randint(0, num_class, [N])
print(tensor)
one_hot = torch.zeros(N, num_class).long()      # torch.zeros()返回一个由标量0填充的张量,里面两个值是张量的尺寸大小 # torch.long():向下取整
one_hot.scatter_(dim=1, index=tensor.unsqueeze(dim=1), src=torch.ones(N, num_class).long())
# dim:表示在第几维上操作     index:索引    src:用来填充/替换原来tensor的值    squeeze：降维     unsqueeze：升维
print(one_hot)
'''

