# 有了MyTestCase以后再写测试用例就不需要重写setUp和tearDown方法
import os

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    """注册模块测试用例"""
    # 因为myTestCase已经实现了setUp和testDown方法,我们以后再写测试用例就不需要重新实现setUp和testDown方法

    def test_zhuce(self):
        """注册功能正向用例"""
        driver=self.driver

        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_link_text("注册").click()
        # driver.current_url #用来获取当前浏览器的网址
        # driver.title #用来获取当前浏览器中的标签页的title
        actual = driver.title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        self.assertEqual(actual, expected)
        base_path = os.path.dirname(__file__)
        path = base_path.replace("day5", "report/image/")
        driver.get_screenshot_as_file(path + "zhuce.png")

