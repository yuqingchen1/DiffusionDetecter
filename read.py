import torch
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# path1 = "/tmp/openai-2022-11-09-15-47-53-716361/samples_16x64x64x3.npz"
# data1 = np.load(path1)
# a = data1['arr_0'][0]
# plt.imshow(a)
# plt.show()
# print(a[0])


import cv2 as cv
import numpy as np
import os


def addimg(imgs, size, layout):
    # imgs为需要展示的图片数组
    # size为展示时每张图片resize的大小
    # layout为展示图片的布局例如（3，3）代表3行3列）
    w = layout[0]
    h = layout[1]
    x = imgs[0].shape[2]
    if w * h - len(imgs) > 0:
        null_img = np.zeros((size[0], size[1], x), dtype='uint8')
        # 注意这里的dtype需要声明为'uint8'，否则和图片矩阵拼接时会导致图片的矩阵失真
        null_img = null_img * 255
    # null_img用来填充当图片数量不足时，布局上缺少的部分
    for i in range(len(imgs)):
        # 和同学交流的过程中发现如果出现有的图片通道不足的时候，会出现合并问题
        # 思考了一下，使用下面这段代码将灰度图片等通道数不足的图片补充成3个通道就ok
        if len(imgs[i].shape) < 3:
            imgs[i] = np.expand_dims(imgs[i], axis=2)
            imgs[i] = np.concatenate((imgs[i], imgs[i], imgs[i]), axis=-1)
        imgs[i] = cv.resize(imgs[i], size)
    for j in range(h):
        for k in range(w):
            if j * w + k > len(imgs) - 1:
                f = k
                while f < w:
                    if f == 0:
                        imgw = null_img
                    else:
                        imgw = np.hstack((imgw, null_img))
                    f = f + 1
                break
            if k == 0:
                imgw = imgs[j * w]
            else:
                imgw = np.hstack((imgw, imgs[j * w + k]))
            print(j * w + k)
        if j == 0:
            imgh = imgw
        else:
            imgh = np.vstack((imgh, imgw))
    return imgh


files = os.listdir('C:/Users/ROG/Desktop/train')
imgs = []
for file in files:
    imgs.append(cv.imread('C:/Users/ROG/Desktop/train/' + str(file)))
imgout = addimg(imgs, (256, 256), (4, 5))
cv.imshow('out', imgout)
cv.waitKey()

# show the details
