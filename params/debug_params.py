"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/4 10:24
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : debug_params.py
@Software  : PyCharm
"""

from enum import Enum


class ParamsTest(Enum):
    # WMS地址
    URL = 'http://192.168.0.173:1888/#/login'
    # 租户ID-xpath
    TENANT = "//input[@placeholder='请输入租户ID']"
    # 租户ID
    TENANT_ID = 'vevor'
    # 账号-xpath
    USERNAME = "//input[@placeholder='请输入账号']"
    # 账号
    NAME = 'wms'
    # 密码-xpath
    PASSWORD = "//input[@placeholder='请输入密码']"
    # 密码
    PWD = 'wms'
    # 验证码-xpath
    VERIFICATION = "//input[@placeholder='请输入验证码']"
    # 验证码
    VERIFICATION_CODE = 'wms'
    # 登录-xpath
    BUTTON = "//span[text()[normalize-space()='登录']]"
    # 窗口大小
    WINDOW_SIZE = {'width': 1920, 'height': 1080}
    # 入库管理
    MANAGEMENT = "//span[text()='入库管理']"
    # 入库单
    RECEIPT = "//span[text()='入库单']"
