import unittest

import time

from day5.myTestCase import MyTestCase
from day6.data_base.connectDB import connDB


class ZhuCeTest(MyTestCase):


    def test_zhuce(self):
        """注册功能正向用例"""
        driver=self.driver

        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("shiji1")
        driver.find_element_by_name("password").send_keys("888888")
        driver.find_element_by_name("userpassword2").send_keys("888888")
        driver.find_element_by_name("mobile_phone").send_keys("13810577894")
        driver.find_element_by_name("email").send_keys("shiji1@qq.com")
        driver.find_element_by_class_name("reg_btn").click()
        time.sleep(3)
        # 检查数据库中新增记录的用户名和我们输入的用户名是否一致
        expected="shiji1"
        actual = connDB()[1]
        self.assertEqual(expected,actual)
        # actual = driver.title
        # expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        # self.assertEqual(actual, expected)
        # base_path = os.path.dirname(__file__)
        # path = base_path.replace("day5", "report/image/")
        # driver.get_screenshot_as_file(path + "zhuce.png")