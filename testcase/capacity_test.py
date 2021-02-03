"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/27 11:43
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : capacity_test.py
@Software  : PyCharm
"""
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config.wms_login import Wms_Login


class Capacity(unittest.TestCase):

    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(r"D:\Tools\vevor\vevor-wms-ui\img"), img_name))

    def setUp(self) -> None:
        self.driver = Wms_Login().test_login()
        self.wait = WebDriverWait(self.driver, 60)

    @BeautifulReport.add_test_img('test_capacity')
    def test_capacity(self):
        """
        产能维护
        """
        self.save_img("test_capacity1")
        # self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='入库管理']")))
        self.driver.find_element_by_xpath("//span[text()='入库管理']").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='入库预约']")))
        self.driver.find_element_by_xpath("//span[text()='入库预约']").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='产能维护']")))
        self.driver.find_element_by_xpath("//span[text()='产能维护']").click()
        self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "(//input[@readonly='readonly'])[1]")))
        self.driver.find_element_by_xpath("(//input[@readonly='readonly'])[1]").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='美国']")))
        self.driver.find_element_by_xpath("//span[text()='美国']").click()
        self.save_img("test_capacity2")
        # self.driver.get_screenshot_as_file('../img/产能维护.png')
        self.save_img("test_capacity3")


def tearDown(self) -> None:
    self.driver.quit()
