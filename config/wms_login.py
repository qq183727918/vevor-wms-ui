"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/26 15:29
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : wms_login.py
@Software  : PyCharm
"""
import time

from selenium import webdriver


class Wms_Login:

    @staticmethod
    def test_login():
        driver = webdriver.Chrome()
        driver.maximize_window()
        # 初次建立连接，随后方可修改cookie
        driver.get('http://192.168.0.173:1888/#/login')
        # 删除第一次建立连接时的cookie
        driver.delete_all_cookies()
        # 输入租户
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='请输入租户ID']").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入租户ID']").send_keys('vevor')
        # 输入账号
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='请输入账号']").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys('wms')
        # 输入密码
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='请输入密码']").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys('wms')
        # 输入验证码
        driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys('11111')
        # 点击登录
        driver.find_element_by_xpath("//span[text()[normalize-space()='登录']]").click()
        time.sleep(3)
        return driver
