

class MemberPage(object):
    # 网页是基于浏览器打开的,所以不能在一个页面创建浏览器
    # 应该把浏览器

    title = "我的会员中心 - 道e坊商城 - Powered by Haidao"

    def __init__(self,driver):
        self.driver = driver


    # def assertEqual(self):
    #     self.actual = self.driver.title()
    #     self.assertEqual(self._title,self.actual)
