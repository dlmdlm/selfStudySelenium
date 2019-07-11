#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: study-selenium
#     FileName: run_tests.py
#         Desc: 
#       Author: Administrator
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2019-07-10 10:26
#=============================================================================
"""

import time, sys
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
sys.path.append('./interface')


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')
# testsuit = defaultTestLoader.discover(test_dir, pattern='credit_query_test.py')


if __name__ == "__main__":

    filepath = "E:/self-study-python/StudySelenium/study-selenium/roport/htmlreport.html"
    # fp = file(filepath, "wb") # python2.7的写法
    fp = open(filepath, mode="wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="this is first report")  # pyton 2.7的写法
    runner = HTMLTestRunner(stream=fp, verbosity=2, title="this is first report")
    runner.run(testsuit)
    fp.close()



