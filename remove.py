import cv2
# import os
#
# from PIL import Image
# from numpy import random
#
#
# def transferPictures(nowpath, newpath):
#     # 将文件夹下的不同类别的文件夹中的部分图片转移到另一个文件夹下的相同类别的文件夹下，并删除原文件夹中的相应图片（类似于剪切）
#     for roots, dirs, files in os.walk(nowpath):
#
#         for i in dirs:
#
#             for roots, dirs, files in os.walk(nowpath + i):
#
#                 fnum = len(files) // 2 #计算一半数量
#                 rdom_files = random.sample(files, fnum) #随机选一半数量的图片
#
#                 for imgname in rdom_files:
#                     imgpath = nowpath + i + '/' + imgname
#                     # print(imgpath)
#                     for roots, dirs, files in os.walk(newpath):
#                         if i in dirs:
#                             im = Image.open(imgpath)
#                             im.save(newpath + i + '/a' + imgname)
#                             os.remove(imgpath)  # 转移完后删除原图片
#
# transferPictures('./data/ImageNet2012/ILSVRC2012_img_val/', './train/')

##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil


def moveFile(fileDir):
    for roots, dirs, files in os.walk(fileDir):
        for j,i in enumerate(dirs):
            for roots, dirs, files in os.walk(fileDir + i):
                pathDir = os.listdir(roots)  # 取图片的原始路径
                filenumber = len(files)
                rate = 0.5  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
                picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
                sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
                print(sample)
                for name in sample:
                    image=cv2.imread(roots +'/'+ name)
                    cv2.imwrite(tarDir+'/'+i+'_'+name,image)
                    # shutil.move(roots +'/'+ name, tarDir )

        return


if __name__ == '__main__':
    fileDir = "./data/ImageNet2012/ILSVRC2012_img_val/"  # 源图片文件夹路径
    tarDir = './train'  # 移动到新的文件夹路径
    moveFile(fileDir)
















