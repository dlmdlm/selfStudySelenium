#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: study-selenium
#     FileName: credit_query_test
#         Desc: 
#       Author: Administrator
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2019-07-10 14:19
#=============================================================================
"""

import time
import unittest
from textwrap import dedent
from selenium.webdriver.common.action_chains import ActionChains

from util.utils import get_driver


class CreditQuery(unittest.TestCase):
    """征信查询"""

    def setUp(self):
        """每个case执行前都会运行
        """
        self.driver = get_driver()

    def test_credit_query(self):
        """征信查询"""
        self.driver.switch_to.default_content()  # 跳到主页面
        self.driver.implicitly_wait(1)  # 休眠一秒钟

        # 点击“待办”按钮
        todo_buttton = self.driver.find_element_by_xpath('//*[@id="remind"]/div[2]/div')
        todo_buttton.click()
        time.sleep(2)

        # 点击“征信查询”按钮
        credit_input = self.driver.find_element_by_xpath('//ul[@id="remind-box"]/li[2]')
        credit_input.click()
        self.driver.implicitly_wait(10)

        # 跳转到征信查询列表的iframe
        # credit_frame = self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[2]/div[2]/iframe[1]')
        credit_frame = self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[2]/div[3]/iframe')
        self.driver.switch_to.frame(credit_frame)
        self.driver.implicitly_wait(10)

        # 选中征信查询订单列表中的订单
        # TODO：如何选中我想要的订单
        # order = self.driver.find_element_by_xpath('//div[@class="layui-table-box"]/div[2]/table/tbody/tr[1]')
        order = self.driver.find_element_by_xpath('//div[@class="layui-table-box"]/div[2]/table/tbody/tr[1]')
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).double_click(order).perform()

        # 跳到-待办/征信查询 编辑页的 iframe
        time.sleep(2)
        add_iframe = self.driver.find_element_by_name('layui-layer-iframe1')
        self.driver.switch_to.frame(add_iframe)
        self.driver.implicitly_wait(10)









        # # 点击提交按钮
        # submit = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]')
        # submit.click()
        # self.driver.implicitly_wait(2)
        # confirm = self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]')  # 确认
        # confirm.click()
        # time.sleep(60)

        # time.sleep(10)  # 观察页面错误
        # # 点击关闭按钮
        # close = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[3]')
        # close.click()
        # self.driver.implicitly_wait(2)
        # confirm = self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]')  # 确认取消
        # confirm.click()

    # def tearDown(self):
    #     """退出
    #     """
    #     # 关闭浏览器
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()