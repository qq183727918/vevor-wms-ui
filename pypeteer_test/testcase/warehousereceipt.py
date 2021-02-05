"""
_*_ coding: UTF-8 _*_
@Time      : 2ParamsTest.MAGICAL.value2ParamsTest.TIME.value/2/4 ParamsTest.TIME.valueParamsTest.MAGICAL.value:22
@Author    : LiuXiaoQiang
@Site      : https://github.com/qqParamsTest.TIME.value837279ParamsTest.TIME.value8
@File      : warehousereceipt.py
@Software  : PyCharm
"""
import asyncio

from pyppeteer import launch
from pytest_pyppeteer.plugin import pyppeteer

from pypeteer_test.params.config_params import ParamsTest
from pypeteer_test.params.warehouse_parmas import Warehouse

pyppeteer.DEBUG = True


async def main():
    driver = await launch(**ParamsTest.PARAMS.value)
    page = await driver.newPage()

    await page.setViewport(ParamsTest.WINDOW_SIZE.value)
    await page.goto(ParamsTest.URL.value)
    try:
        # 输入租户ID
        click_handle = await page.xpath(ParamsTest.TENANT.value)
        print(F'租户ID:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].type(ParamsTest.TENANT_ID.value)
        await asyncio.sleep(ParamsTest.TIME.value)
        # 输入账号
        click_handle = await page.xpath(ParamsTest.USERNAME.value)
        print(F'账号:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].type(ParamsTest.NAME.value)
        await asyncio.sleep(ParamsTest.TIME.value)
        # 输入密码
        click_handle = await page.xpath(ParamsTest.PASSWORD.value)
        print(F'密码:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].type(ParamsTest.PWD.value)
        # 输入验证码
        click_handle = await page.xpath(ParamsTest.VERIFICATION.value)
        print(F'验证码:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].type(ParamsTest.VERIFICATION_CODE.value
                                                          # ,{'delay': ParamsTest.WAITING.value}
                                                          )
        # 点击登录按钮
        click_handle = await page.xpath(ParamsTest.BUTTON.value)
        print(F'登录按钮:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].click()
        await asyncio.sleep(ParamsTest.TIME.value)
        # 点击入库管理
        click_handle = await page.xpath(ParamsTest.MANAGEMENT.value)
        print(F'入库管理:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].click()
        await asyncio.sleep(ParamsTest.TIME.value)
        # 点击入库单
        click_handle = await page.xpath(ParamsTest.RECEIPT.value)
        print(F'入库单:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].click()
        await asyncio.sleep(ParamsTest.TIME.value)
        # 入库单号
        click_handle = await page.xpath(Warehouse.RECEIPT.value)
        print(F'入库单号:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].type(Warehouse.RECEIPT_NUM.value)
        await asyncio.sleep(ParamsTest.TIME.value)
        # # 客户
        # click_handle = await page.xpath(Warehouse.CUSTOMER.value)
        # print(F'客户:{click_handle}')
        # await click_handle[ParamsTest.MAGICAL.value].click()
        # await asyncio.sleep(ParamsTest.TIME.value)
        # # 运输方式
        # click_handle = await page.xpath(Warehouse.TRANSPORT.value)
        # print(F'运输方式:{click_handle}')
        # await click_handle[ParamsTest.MAGICAL.value].type(Warehouse.RECEIPT_NUM.value, {'delay': ParamsTest.WAITING.value})
        # # 状态
        # click_handle = await page.xpath(Warehouse.STATUS.value)
        # print(F'状态:{click_handle}')
        # await click_handle[ParamsTest.MAGICAL.value].type(Warehouse.RECEIPT_NUM.value, {'delay': ParamsTest.WAITING.value})
        # # 目的仓
        # click_handle = await page.xpath(Warehouse.DESTINATION.value)
        # print(F'目的仓:{click_handle}')
        # await click_handle[ParamsTest.MAGICAL.value].type(Warehouse.RECEIPT_NUM.value, {'delay': ParamsTest.WAITING.value})
        # # 开始时间
        # click_handle = await page.xpath(Warehouse.STARTING.value)
        # print(F'开始时间:{click_handle}')
        # await click_handle[ParamsTest.MAGICAL.value].type(Warehouse.RECEIPT_NUM.value, {'delay': ParamsTest.WAITING.value})
        # # 结束时间
        # click_handle = await page.xpath(Warehouse.ENDING.value)
        # print(F'结束时间:{click_handle}')
        # await click_handle[ParamsTest.MAGICAL.value].type(Warehouse.RECEIPT_NUM.value, {'delay': ParamsTest.WAITING.value})
        # 查询
        click_handle = await page.xpath(Warehouse.SELECT.value)
        print(F'查询:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].click()
        await asyncio.sleep(ParamsTest.TIME.value)
        # 详情
        click_handle = await page.xpath(Warehouse.DETAIL.value)
        print(F'详情:{click_handle}')
        await click_handle[ParamsTest.MAGICAL.value].click()
        await asyncio.sleep(ParamsTest.TIME.value)
        await driver.close()
    except Exception as e:
        print(f'错误信息：{e}')
        # 截图保存
        await page.screenshot({'path': './example.png'})
class Login:
    asyncio.get_event_loop().run_until_complete(main())
