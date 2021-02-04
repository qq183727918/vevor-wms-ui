"""
_*_ coding: UTF-8 _*_
@Time      : 2021/1/25 19:36
@Author    : LiuXiaoQiang
@Site      : https://github.com/qq183727918
@File      : run.py
@Software  : PyCharm
"""

import unittest
import time
from BeautifulReport import BeautifulReport
sleep = time.strftime("%Y-%m-%d", time.localtime())
# 用例存放位置
test_case_path = r"D:\Tools\vevor\vevor-wms-ui\testcase"
# 测试报告存放位置
log_path = r'D:\Tools\vevor\vevor-wms-ui\reports'
# 测试报告名称
filename = f'WMS测试报告{sleep}'
# 用例名称
description = 'WMS测试'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern = "warehouse_test.py"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description=description, report_dir=log_path)
