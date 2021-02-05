"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/4 10:24
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : config_params.py
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
    # pyppeteer参数
    PARAMS = {
        # 关闭无头浏览器
        "headless": False,
        'dumpio': 'True',  # 防止浏览器卡住
        r'userDataDir': './cache-data',  # 用户文件地址
        "args": [
            '--disable-infobars',  # 关闭自动化提示框
            '--window-size=1920,1080',  # 窗口大小
            '--log-level=30',  # 日志保存等级， 建议设置越小越好，要不然生成的日志占用的空间会很大 30为warning级别
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            '--no-sandbox',  # 关闭沙盒模式
            '--start-maximized',  # 窗口最大化模式
            # '--proxy-server=http://localhost:1080'  # 代理
        ],
    }
    # 时间
    TIME = 1
    # 魔法值
    MAGICAL = 0
    # 等待时间
    WAITING = 100

