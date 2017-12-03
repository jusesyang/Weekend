import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit

