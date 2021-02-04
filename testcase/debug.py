"""
_*_ coding: UTF-8 _*_
@Time      : 2021/2/4 10:22
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : debug.py
@Software  : PyCharm
"""
import asyncio

from pyppeteer import launch
from pytest_pyppeteer.plugin import pyppeteer

from params.debug_params import ParamsTest
from params.warehouse_parmas import Warehouse

pyppeteer.DEBUG = True


async def main():
    driver = await launch(**ParamsTest.PARAMS.value)
    page = await driver.newPage()

    await page.setViewport(ParamsTest.WINDOW_SIZE.value)
    await page.goto(ParamsTest.URL.value)

    # 输入租户ID
    click_handle = await page.xpath(ParamsTest.TENANT.value)
    print(F'输入租户ID:{click_handle}')
    await click_handle[0].type(ParamsTest.TENANT_ID.value, {'delay': 100})
    await asyncio.sleep(1)
    # 输入账号
    click_handle = await page.xpath(ParamsTest.USERNAME.value)
    print(F'输入账号:{click_handle}')
    await click_handle[0].type(ParamsTest.NAME.value, {'delay': 100})
    await asyncio.sleep(1)
    # 输入密码
    click_handle = await page.xpath(ParamsTest.PASSWORD.value)
    print(F'输入密码:{click_handle}')
    await click_handle[0].type(ParamsTest.PWD.value, {'delay': 100})
    # 输入验证码
    click_handle = await page.xpath(ParamsTest.VERIFICATION.value)
    print(F'输入验证码:{click_handle}')
    await click_handle[0].type(ParamsTest.VERIFICATION_CODE.value, {'delay': 100})
    # 点击登录按钮
    click_handle = await page.xpath(ParamsTest.BUTTON.value)
    print(F'点击登录按钮:{click_handle}')
    await click_handle[0].click()
    await asyncio.sleep(2)
    # 点击入库管理
    click_handle = await page.xpath(ParamsTest.MANAGEMENT.value)
    print(F'点击入库管理:{click_handle}')
    await click_handle[0].click()
    await asyncio.sleep(1)
    # 点击入库单
    click_handle = await page.xpath(ParamsTest.RECEIPT.value)
    print(F'点击入库单:{click_handle}')
    await click_handle[0].click()
    await asyncio.sleep(1)
    # 入库单号
    click_handle = await page.xpath(Warehouse.RECEIPT.value)
    print(F'入库单号:{click_handle}')
    await click_handle[0].type(Warehouse.RECEIPT_NUM.value, {'delay': 100})
    # 查询
    click_handle = await page.xpath(Warehouse.SELECT.value)
    print(F'查询:{click_handle}')
    await click_handle[0].click()
    await asyncio.sleep(1)


    await driver.close()


class Login:
    asyncio.get_event_loop().run_until_complete(main())
