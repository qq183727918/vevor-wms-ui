"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/4 16:19
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : see.py
@Software  : PyCharm
"""
from PIL import Image
import pytesseract


def image_str(images):
    image = Image.open(images)
    result = pytesseract.image_to_string(image, lang='eng')  # 图片转文字
    print(result)  # 打印识别的验证码


image_str('./emoji1.png')
