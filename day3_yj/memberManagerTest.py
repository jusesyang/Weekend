
import unittest

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MemberManagerTest(unittest.TestCase):

    # 变量前边加上self表示这个变量是类的属性可以被所有的方法访问
    def setUp(self):
        self.driver = webdriver.Chrome()
        # driver声明在setUp方法之内,不能被其他方法访问
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        # close是关闭一个浏览器标签,quit是关闭整个浏览器
        # 代码编写和调试时需要在quit方法前加时间等待,方便看清楚执行过程
        # 正式运行时去掉时间等待,为了提高程序执行速度
        time.sleep(10)
        self.driver.quit()

    def test_add_member(self):
        driver=self.driver
        login_url = "http://localhost/index.php?&m=admin&c=public&a=login"
        driver.get(login_url)
        user_name = "admin"
        user_pwd = "password"
        verify_no = "1234"
        # 1.登录
        driver.find_element_by_name("username").send_keys(user_name)
        driver.find_element_by_name("userpass").send_keys(user_pwd)
        driver.find_element_by_name("userverify").send_keys(verify_no)
        driver.find_element_by_class_name("Btn").click()

        # 2.会员管理
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        time.sleep(3)
        # 3.添加会员信息

        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("yanglengleng")
        driver.find_element_by_name("mobile_phone").send_keys("18210574568")
        driver.find_element_by_css_selector('[name=sex][value="1"]').click()
        driver.find_element_by_id("birthday").send_keys("1990-12-12")
        driver.find_element_by_name("email").send_keys("yll@qq.com")
        driver.find_element_by_name("qq").click()
        driver.find_element_by_class_name("button_search").click()
