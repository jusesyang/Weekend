import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.memberPage import MemberPage


class LoginTest(MyTestCase):

    # def test_login(self):
    #     # 1.打开网页
    #     self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
    #     # 2.输入用户名
    #     self.driver.find_element(By.ID,"username").send_keys("shiji")
    #     # 3.输入密码
    #     self.driver.find_element(By.ID,"password").send_keys("888888")
    #     # 4.点击登录按钮
    #     self.driver.find_element(By.CLASS_NAME,"login_btn").click()
    #     # 5.验证是否跳转到管理中心页面
    #     time.sleep(3)
    #
    #     actual = self.driver.title

    #     self.assertIn(expected,actual)
    def test_login(self):
        lp = LoginPage(self.driver)
        lp.open()
        lp.input_username("shiji")
        lp.input_password("888888")
        lp.click_login_btn()

        mp = MemberPage(self.driver)
        expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        self.assertEqual(expected,mp.tilte)