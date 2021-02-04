"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/4 13:17
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : warehouse_parmas.py
@Software  : PyCharm
"""
from enum import Enum


class Warehouse(Enum):
    # 入库单
    RECEIPT = "//input[@placeholder='入库单号']"
    # 入库单号
    RECEIPT_NUM = "RK2021020100000576"
    # 客户
    CUSTOMER = "//input[@placeholder='客户']"
    # 运输方式
    tRANSPORT = "//input[@placeholder='运输方式']"
    # 状态
    STATUS = "//input[@placeholder='状态']"
    # 目的仓
    DESTINATION = "//input[@placeholder='目的仓']"
    # 开始时间
    STARTING = "//input[@placeholder='开始日期']"
    # 结束时间
    ENDING = "//input[@placeholder='结束日期']"
    # 查询
    SELECT = "//span[text()='搜 索']"
    # 详情
    DETAIL = "//div[@id='avue-view']/div[1]/div[1]/div[1]/div[1]/div[3]/div[4]/div[2]/table[1]/tbody[1]/tr[1]/td[10]/div[1]/button[1]/span[1]"
