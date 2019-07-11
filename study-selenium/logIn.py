# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
#=============================================================================
#  ProjectName: Automath the boring stuff with python
#       Create: 2019-04-09 15:16
#     FileName: login.py
#         Desc: 登录车贷管理系统
#       Author: dlm
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
"""

from __future__ import print_function

import time
import unittest

from selenium import webdriver


class TestLogin(unittest.TestCase):
    """登录测试"""

    def setUp(self):
        """每个case执行前都会运行"""
        self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(15)
        self.driver.get("http://channel.yuuwei.com/admin/login/index.html")
        # self.driver.implicitly_wait(5)

    def login(self, username, password):
        """登录"""

        # 输入账户名
        self.driver.find_element_by_name("user_name").clear()
        self.driver.find_element_by_name("user_name").send_keys(username)
        self.driver.implicitly_wait(10)

        # 输入密码
        self.driver.find_element_by_name("user_password").clear()
        self.driver.find_element_by_name("user_password").send_keys(password)
        self.driver.implicitly_wait(10)

        # 点击登录按钮
        self.driver.find_element_by_tag_name("button").click()

    def test01(self):
        """正确用户名密码
        """
        self.login("chjt", "1234567")
        self.driver.implicitly_wait(10)

        # 登录之后跳转的iframe[@data-id="0"]
        xf = self.driver.find_element_by_xpath('//iframe[@data-id="0"]')
        self.driver.switch_to.frame(xf)

        # 登录成功之后的断言
        login_success = self.driver.find_element_by_class_name("layui-text").text
        self.assertIn(u'宇为科技竭诚为您服务', login_success, msg=u'宇为科技竭诚为您服务')

        # 跳出iframe[@data-id="0"]到主页
        self.driver.switch_to.default_content()
        time.sleep(1)

        # 获取左边导航栏
        # TODO:左边导航栏要判断一下，啥时候没有显示出来要点击按钮才会出来
        side = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]")
        print("左边导航栏宽度: ", side.value_of_css_property("width"))

        # 点击出现菜单栏icon，出现左边菜单栏（要先点击父级，再点击该按钮，才可成功，所以有两个click）
        self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[1]').click()
        icon = self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[1]/i')
        icon.click()

        # 点击左边菜单栏-【车贷流程】按钮
        self.driver.find_element_by_xpath('//*[@id="submenu"]/div[1]/ul/li[1]/dl/dd/a/span').click()

        # 跳转到【车贷流程-新增征信】的iframe
        addcredit_frame = self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(addcredit_frame)

        # 点击[车贷流程-【新增征信】]按钮 ，先找到父亲节点，再回来
        zhenxin_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/section/section/div[2]')
        zhenxin_button.click()
        new_zhenxin = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/section/section/div[2]/button')
        new_zhenxin.click()

        # dlm想通过这个找到-新增征信的编辑页，但是一直报错获取失败
        # add_iframe = self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/iframe[1]')

        # gege help后，是这样找的
        crediteditor_iframe = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/iframe[1]')
        self.driver.switch_to.frame(crediteditor_iframe)

        # 选择银行
        bank = self.driver.find_element_by_xpath('//*[@name="JOB17037"]')
        bank.click()
        time.sleep(2)

        # 选择工行贵州支行
        sub_bank = self.driver.find_element_by_xpath('//*[@id="codeList_single_1_span"]')
        sub_bank.click()

        # 输入客户姓名
        self.driver.find_element_by_name("JOB17038").clear()
        self.driver.find_element_by_name("JOB17038").send_keys("test123456")

        # 输入客户身份证号码
        self.driver.find_element_by_name("JOB17040").clear()
        self.driver.find_element_by_name("JOB17040").send_keys("360732199511223344")

        # 输入客户手机号码
        self.driver.find_element_by_name("JOB17041").clear()
        self.driver.find_element_by_name("JOB17041").send_keys("18712341234")

        # 点击身份证正面
        id_card_path = "id_card.jpeg"
        id_card__button = self.driver.find_element_by_xpath('//*[@id="JOB17051_up"]')
        id_card__button.click()
        # id_card__button.send_keys(id_card_path)

    # def tearDown(self):
    #     """退出
    #     """
    #     time.sleep(5)
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
