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

from params import debug_params

pyppeteer.DEBUG = True
params = debug_params.ParamsTest()


async def main():
    driver = await launch(headless=False)

    page = await driver.newPage()

    await page.setViewport(params.Window_size())
    await page.goto(params.url())

    # 输入租户ID
    click_handle = await page.xpath(params.tenantID())
    await click_handle[0].type(params.tenant_ID())
    # 输入账号
    click_handle = await page.xpath(params.username())
    await click_handle[0].type(params.name())
    # 输入密码
    click_handle = await page.xpath(params.password())
    await click_handle[0].type(params.pwd())
    # 输入验证码
    click_handle = await page.xpath(params.verification_Code())
    await click_handle[0].type(params.verificationCode())
    # 点击搜索按钮
    click_handle = await page.xpath(params.button())
    await click_handle[0].click()
    # 点击入库管理
    # 点击入库单
    await asyncio.sleep(2)

    await driver.close()


class Login:
    asyncio.get_event_loop().run_until_complete(main())
