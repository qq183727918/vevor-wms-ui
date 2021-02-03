"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/29 10:14
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : save_img.py
@Software  : PyCharm
"""
import os


def save_img(driver, img_name):  # 错误截图方法，这个必须先定义好
    """
        传入一个img_name, 并存储到默认的文件路径下
    :param driver:
    :param img_name:
    :return:
    """
    driver.get_screenshot_as_file(
        '{}/{}.png'.format(os.path.abspath(r"D:\Tools\vevor\vevor-wms-ui\img"), img_name))
