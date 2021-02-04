"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/3 19:06
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : warehouse_test.py
@Software  : PyCharm
"""
import os
import time
import unittest

from BeautifulReport import BeautifulReport
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config.wms_login import Wms_Login


class Warehouse(unittest.TestCase):

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

    @BeautifulReport.add_test_img("test_warehouse")
    def test_warehouse(self):
        """
        入库单
        """
        # 点击入库管理
        self.wait_time("//span[text()='入库管理']")
        self.driver.find_element_by_xpath("//span[text()='入库管理']").click()
        # 点击入库单
        self.wait_time("//span[text()='入库单']")
        self.driver.find_element_by_xpath("//span[text()='入库单']").click()
        # 入库单号
        self.wait_time("//input[@placeholder='入库单号']")
        self.driver.find_element_by_xpath("//input[@placeholder='入库单号']").send_keys('RK2021020100000177')
        self.select_test()
        Inbound = self.driver.find_element_by_xpath("(//div[@class='cell']//span)[2]").text
        print(Inbound)
        self.save_img("Warehouse_test_warehouse")
        assert Inbound == 'RK2021020100000177'
        time.sleep(1)
        # 客户
        self.wait_time("//input[@placeholder='客户']")
        self.driver.find_element_by_xpath("//input[@placeholder='客户']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='客户']").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("//input[@placeholder='客户']").send_keys(Keys.ENTER)
        # self.select_test()
        # customer = self.driver.find_element_by_xpath("//li[@class='el-select-dropdown__item hover']//span[1]").text
        # print(customer)
        # self.save_img("Warehouse_test_warehouse")
        # assert customer == '上海司顺电子商务有限公司'
        time.sleep(1)
        # 运输方式
        self.wait_time("//input[@placeholder='运输方式']")
        self.driver.find_element_by_xpath("//input[@placeholder='运输方式']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='运输方式']").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("//input[@placeholder='运输方式']").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("//input[@placeholder='运输方式']").send_keys(Keys.ENTER)
        # self.select_test()
        # transport = self.driver.find_element_by_xpath("(//li[@class='el-select-dropdown__item hover'])[2]").text
        # self.save_img("Warehouse_test_warehouse")
        # assert transport == '卡车'
        time.sleep(1)
        # 状态
        self.wait_time("//input[@placeholder='状态']")
        self.driver.find_element_by_xpath("//input[@placeholder='状态']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='状态']").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("//input[@placeholder='状态']").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("//input[@placeholder='状态']").send_keys(Keys.ENTER)
        # self.select_test()
        # status = self.driver.find_element_by_xpath(
        #     "(//li[contains(@class,'el-select-dropdown__item selected')])[2]").text
        #
        # self.save_img("Warehouse_test_warehouse")
        # assert status == '作业中'
        time.sleep(1)
        # 目的仓
        self.wait_time("//input[@placeholder='目的仓']")
        self.driver.find_element_by_xpath("//input[@placeholder='目的仓']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='目的仓']").send_keys(Keys.DOWN)
        self.driver.find_element_by_xpath("//input[@placeholder='目的仓']").send_keys(Keys.ENTER)
        self.select_test()
        # warehouse = self.driver.find_element_by_xpath("(//li[@class='el-select-dropdown__item hover']//span)[3]").text
        # self.save_img("Warehouse_test_warehouse")
        # assert warehouse == '美西CA-USSR司顺洛杉矶仓'
        time.sleep(1)
        # 创建时间
        self.wait_time("//input[@placeholder='开始日期']")
        self.driver.find_element_by_xpath("//input[@placeholder='开始日期']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='开始日期']").send_keys('2021-02-01 00:00:00')
        self.wait_time("//input[@placeholder='结束日期']")
        self.driver.find_element_by_xpath("//input[@placeholder='结束日期']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='结束日期']").send_keys('2021-02-10 00:00:00')
        self.select_test()

    def select_test(self):
        # 查询
        self.driver.find_element_by_xpath("//span[text()='搜 索']").click()

    def wait_time(self, path):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, path)))


def tearDown(self) -> None:
    self.driver.quit()
