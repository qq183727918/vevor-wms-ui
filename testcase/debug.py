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
    driver = await launch(headless=False, args=['--disable-infobars'], dumpio=True)
    page = await driver.newPage()

    await page.setViewport(ParamsTest.WINDOW_SIZE.value)
    await page.goto(ParamsTest.URL.value)

    # 输入租户ID
    click_handle = await page.xpath(ParamsTest.TENANT.value)
    print(click_handle)
    await click_handle[0].type(ParamsTest.TENANT_ID.value)
    await asyncio.sleep(1)
    # 输入账号
    click_handle = await page.xpath(ParamsTest.USERNAME.value)
    print(click_handle)
    await click_handle[0].type(ParamsTest.NAME.value)
    await asyncio.sleep(1)
    # 输入密码
    click_handle = await page.xpath(ParamsTest.PASSWORD.value)
    print(click_handle)
    await click_handle[0].type(ParamsTest.PWD.value)
    # 输入验证码
    click_handle = await page.xpath(ParamsTest.VERIFICATION.value)
    print(click_handle)
    await click_handle[0].type(ParamsTest.VERIFICATION_CODE.value)
    # 点击登录按钮
    click_handle = await page.xpath(ParamsTest.BUTTON.value)
    print(click_handle)
    await click_handle[0].click()
    await asyncio.sleep(2)
    # 点击入库管理
    click_handle = await page.xpath(ParamsTest.MANAGEMENT.value)
    print(click_handle)
    await click_handle[0].click()
    await asyncio.sleep(1)
    # 点击入库单
    click_handle = await page.xpath(ParamsTest.RECEIPT.value)
    print(click_handle)
    await click_handle[0].click()
    await asyncio.sleep(1)
    # 入库单号
    click_handle = await page.xpath(Warehouse.RECEIPT.value)
    print(click_handle)
    await click_handle[0].type(Warehouse.RECEIPT_NUM.value)
    # 查询
    click_handle = await page.xpath(Warehouse.SELECT.value)
    print(click_handle)
    await click_handle[0].click()
    await asyncio.sleep(1)
    await driver.close()


class Login:
    asyncio.get_event_loop().run_until_complete(main())
