# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
#=============================================================================
#       Create: 2019-07-04 11:16
#     FileName: login.py
#         Desc: 新建征信
#       Author: dlm
#        Email: 136665323@qq.com
#     HomePage: dlmdlm.github.io
#=============================================================================
"""

from __future__ import print_function

import time
import unittest

from textwrap import dedent

from selenium import webdriver


class TestNewCredit(unittest.TestCase):
    """新建征信"""

    def setUp(self):
        """每个case执行前都会运行
        """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()  # 把浏览器窗口最大化
        self.driver.implicitly_wait(15)  # 隐性等待页面加载，最长时间为15秒
        # TODO: 注意不要把产品地址提交到GitHub上了
        self.driver.get("http://saas.chedai0.com/admin/index/index.html")  # 在浏览器打开页面
        self.driver.implicitly_wait(5)
        self.login("****", "1#####")  # TODO: 注意不要把用户名密码提交到GitHub上了

    def login(self, username, password):
        """登录
        """
        # 输入用户名
        self.driver.find_element_by_name("user_name").clear()
        self.driver.find_element_by_name("user_name").send_keys(username)
        self.driver.implicitly_wait(1)

        # 输入密码
        self.driver.find_element_by_name("user_password").clear()
        self.driver.find_element_by_name("user_password").send_keys(password)
        self.driver.implicitly_wait(1)

        # 点击登录按钮
        self.driver.find_element_by_tag_name("button").click()

    def test_new_credit(self):
        """正确用户名密码
        """
        # self.driver.implicitly_wait(10)
        
        xf = self.driver.find_element_by_xpath('//iframe[@data-id="0"]')
        self.driver.switch_to.frame(xf)
        login_success = self.driver.find_element_by_class_name("layui-text").text
        self.assertIn(u'宇为科技竭诚为您服务', login_success, msg=u'宇为科技竭诚为您服务')
        self.driver.switch_to.default_content()  # 跳到主页面
        self.driver.implicitly_wait(1)  # 休眠一秒钟

        side = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]")  # 获取左边导航栏
        print("左边导航栏宽度: ", side.value_of_css_property("width"))  # 打印出左边导航栏的宽
        # TODO:左边导航栏要判断一下，啥时候没有显示出来，要点击按钮才会出来
        # if side.value_of_css_property("width") == "200px":
        #     self.driver.find_element_by_xpath('//*[@id="submenu"]/div[1]/ul/li[1]/dl/dd').click()
        #     print(side.value_of_css_property("width"))

        # icon = self.driver.find_element_by_xpath('//div[@id="jqadmin-tab"]/div[1]')  # 欧巴教的
        # TODO: 暂时先点两次，后续优化 （73.74代码已经优化，click事件无效，先获取该元素父级点击，再获取该元素点击）
        # icon.click()  # 点击“icon”出现左边导航栏
        # icon.click()  # 点击“icon”出现左边导航栏
        self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[1]').click()
        self.driver.implicitly_wait(1)
        icon = self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[1]/i')
        icon.click()  # 因为当时调试的原因，gege tech 分开，就可以排除问题

        self.driver.find_element_by_xpath('//*[@id="submenu"]/div[1]/ul/li[1]/dl/dd/a/span').click()  # 点击[车贷流程] 按钮

        # 跳到-车贷流程/新增征信 列表页的 iframe
        credit_frame = self.driver.find_element_by_xpath('//*[@id="jqadmin-tab"]/div[2]/div[2]/iframe')
        self.driver.switch_to.frame(credit_frame)

        # 点击 -新增征信列表页中的[新增征信] 按钮（先找到父亲点击，再找到本元素点击，click事件才能生效）
        credit_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/section/section/div[2]')
        credit_button.click()
        new_credit = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/section/section/div[2]/button')
        new_credit.click()

        # 跳到-车贷流程/新增征信 编辑页的 iframe
        add_iframe = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/iframe[1]')
        self.driver.switch_to.frame(add_iframe)
        self.driver.implicitly_wait(10)

        # 选择银行
        bank = self.driver.find_element_by_xpath('//*[@name="JOB02001"]')
        bank.click()

        # 选择工行银行
        sub_bank = self.driver.find_element_by_xpath('//*[@id="codeList_single_1_a"]')
        sub_bank.click()

        # 选择产品名称
        project_name = self.driver.find_element_by_xpath('//*[@id="JOB02062"]')
        project_name .click()

        # 选择快乐购
        sub_project_name = self.driver.find_element_by_xpath('//*[@id="codeList_single_1_a"]')
        sub_project_name.click()

        # 输入客户姓名
        self.driver.find_element_by_name("JOB02002").clear()
        self.driver.find_element_by_name("JOB02002").send_keys("test123456")
        time.sleep(2)

        # 输入客户身份证号码
        self.driver.find_element_by_name("JOB02003").clear()
        self.driver.find_element_by_name("JOB02003").send_keys("230405197001080013")
        time.sleep(2)

        # 输入客户手机号码
        self.driver.find_element_by_name("JOB02004").clear()
        self.driver.find_element_by_name("JOB02004").send_keys("18712341234")
        time.sleep(2)

        # 禁止文件选择器从窗口弹出
        self.driver.execute_script(
            dedent("""\
            document.addEventListener('click', function(evt) {
              if (evt.target.type === 'file')
                evt.preventDefault();
            }, true)
            """)
        )

        # 上传身份证正面图片
        id_card_positive_button = self.driver.find_element_by_xpath('//*[@id="JOB02005_up"]')
        id_card_positive_button.click()
        id_card_positive_path = "C:\Denglimei\work\photo\\153205319914634200.jpg"  # 身份证正面图片路径
        self.driver.find_elements_by_css_selector('input[type=file]')[0].send_keys(id_card_positive_path)
        time.sleep(2)

        # 上传身份证背面图片
        id_card_back_button = self.driver.find_element_by_xpath('//*[@id="JOB02006_up"]')
        id_card_back_button.click()
        id_card_back_path = "C:\Denglimei\work\photo\\153205319914634200.jpg"  # 身份证背面图片路径
        self.driver.find_elements_by_css_selector('input[type=file]')[1].send_keys(id_card_back_path)
        time.sleep(2)

        self.driver.switch_to.default_content()  # 先跳到主页面
        self.driver.switch_to.frame(credit_frame)  # 跳到征信页面

        # 点击提交按钮
        submit = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]')
        submit.click()
        self.driver.implicitly_wait(2)
        confirm = self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]')  # 确认
        confirm.click()


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
