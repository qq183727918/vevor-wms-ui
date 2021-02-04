"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/4 10:24
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : debug_params.py
@Software  : PyCharm
"""


class ParamsTest:
    @staticmethod
    def url():
        """
        WMS地址
        :return
        """
        url = 'http://192.168.0.173:1888/#/login'
        return url

    @staticmethod
    def tenantID():
        """
        租户ID-xpath
        :return
        """
        tenantID = "//input[@placeholder='请输入租户ID']"
        return tenantID

    @staticmethod
    def tenant_ID():
        """
        租户ID
        :return
        """
        tenant_ID = 'vevor'
        return tenant_ID

    @staticmethod
    def username():
        """
        账号-xpath
        :return
        """
        username = "//input[@placeholder='请输入账号']"
        return username

    @staticmethod
    def name():
        """
        账号
        :return:
        """
        name = 'wms'
        return name

    @staticmethod
    def password():
        """
        密码-xpath
        :return
        """
        password = "//input[@placeholder='请输入密码']"
        return password

    @staticmethod
    def pwd():
        """
        密码
        :return:
        """
        pwd = 'wms'
        return pwd

    @staticmethod
    def verification_Code():
        """
        验证码-xpath
        :return:
        """
        verification_Code = "//input[@placeholder='请输入验证码']"
        return verification_Code

    @staticmethod
    def verificationCode():
        """
        验证码
        :return:
        """
        verificationCode = 'wms'
        return verificationCode

    @staticmethod
    def button():
        """
        登录-xpath
        :return:
        """
        button = "//span[text()[normalize-space()='登录']]"
        return button

    @staticmethod
    def Window_size():
        """
        窗口大小
        :return:
        """
        Window_size = {
            'width': 1920,
            'height': 1080
        }
        return Window_size
