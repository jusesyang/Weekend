import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(object):
    # 构造方法的作用
    # 实例化LoginPage的时候需要把driver,作为参数传进来,便于其他属性和方法使用driver

    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_btn_loc = (By.CLASS_NAME,"login_btn")

    def __init__(self,driver):
        self.driver = driver


    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        # self.driver.find_element_by_id("username").send_keys(username)
        # self.driver.find_element(By.ID,"username").send_keys(username)
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        # self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_btn(self):
        self.driver.find_element(*self.login_btn_loc).click()
        time.sleep(3)
