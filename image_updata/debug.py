"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/4 15:14
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : warehousereceipt.py
@Software  : PyCharm
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def plt_show(img):
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imageRGB)
    plt.show()


image = cv2.imread('emg.png', 0)  # 导入灰度图即可
plt_show(image)

ret, image_binary = cv2.threshold(image, 180, 105, cv2.THRESH_BINARY)
plt_show(image_binary)

cv2.imwrite('./emoji1.png', np.array(image_binary))

