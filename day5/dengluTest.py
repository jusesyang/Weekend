import unittest

import time
from selenium import webdriver

from day5.myTestCase import MyTestCase


class DengLuTest(MyTestCase):
    """登录模块测试用例"""





    def test_denglu(self):
        """登录功能正常情况的用例"""
        driver = self.driver
        # 打开登录页面
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 输入用户名
        driver.find_element_by_id("username").send_keys("yll")
        # 输入密码
        driver.find_element_by_id("password").send_keys("888888")
        driver.find_element_by_class_name("login_btn").click()
        time.sleep(2)
        act=driver.find_element_by_link_text("您好 yll").text
        self.assertEqual(act,"您好 yll")
        print("当前用户名:yll:,用户密码:888888")

if __name__ == '__main__':
    unittest.main()


