#!/usr/bin/env python
# -*- coding -*-

from selenium import webdriver
global driver
driver = None


def login(driver, username, password):
    """登录
    """
    # 输入用户名
    driver.find_element_by_name("user_name").clear()
    driver.find_element_by_name("user_name").send_keys(username)
    driver.implicitly_wait(1)

    # 输入密码
    driver.find_element_by_name("user_password").clear()
    driver.find_element_by_name("user_password").send_keys(password)
    driver.implicitly_wait(1)

    # 点击登录按钮
    driver.find_element_by_tag_name("button").click()


def get_driver():
    global driver
    if driver:
        return driver
    driver = webdriver.Chrome()
    driver.maximize_window()  # 把浏览器窗口最大化
    # driver.implicitly_wait(15)  # 隐性等待页面加载，最长时间为15秒
    # TODO: 注意不要把产品地址提交到GitHub上了
    driver.get("http://saas.chedai0.com/admin/index/index.html")  # 在浏览器打开页面
    driver.implicitly_wait(5)
    login(driver, "####", "####")  # TODO: 注意不要把用户名密码提交到GitHub上了
    return driver

get_driver()