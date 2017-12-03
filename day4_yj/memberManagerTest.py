
import time
# 1.导入ddt
import ddt
from selenium import webdriver
import unittest
from day4 import readCSV2
from day4.readCSV2 import read
# 2.装饰这个类
@ddt.ddt
class MemberManagerTest(unittest.TestCase):
    # 3.调用之前写好的read()方法,获取文件中的数据
    member_info=read("member_info.csv")

    @classmethod
    def setUpClass(cls):
        print("所有方法之前执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        print("测试结束关闭浏览器")
        cls.driver.quit()


    def test_alogin(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        user_name = "admin"
        user_pwd = "password"
        verify_no = "1234"
        # 1.登录
        driver.find_element_by_name("username").send_keys(user_name)
        driver.find_element_by_name("userpass").send_keys(user_pwd)
        driver.find_element_by_name("userverify").send_keys(verify_no)
        driver.find_element_by_class_name("Btn").click()
        time.sleep(3)
    # python中集合前面的*,表示把集合中的所有元素拆开一个一个写
    # 5.加入一个方法需要接收2个参数,那么可能不能传一个list进去,但是如果list中正好也是2个元素这时在列表前边加一个*就可以传进去了
    # 测试数据来源于read(),把数据表中的每一行传入方法,在方法中增加一个参数
    @ddt.data(*member_info)
    def test_b_add_member(self,row):
        # 每组测试用例就是一组测试用例,每条测试用例应该是独立的,不能因为上一条测试用例失败,导致下一组数据不能被执行
        # 这里不推荐用for循环,改变代码缩进
        # 应该用ddt装饰器,去修饰这个方法,达到每条测试用例独立执行的目的
        driver = self.driver
        # print("添加会员")
        # 4.注释掉for循环
        # for row in read("member_info.csv"):
        print("添加会员%s" %row)
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        time.sleep(3)
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector('[value="%s"]' % row[2]).click()
        # driver.find_element_by_css_selector('[value="'+row[2]+'"]').click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        time.sleep(3)
        # 之前的代码是能够自动运行,但是还不能自动判断程序运行的是否正确
        # 我们的自动化代码不能找人总是看着运行
        # actual实际结果,执行测试用例以后,页面上实际显示的结果
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        expected = row[0]
        # expected 期望结果,来自于手动测试用例或者是需求文档,配置文件
        driver.switch_to.default_content()
        # 断言和if语句类似于if else语句是用来做判断的
        # if actual==expected:
        #     print("test pass!")
        # else:
        #     print("test fail...")
        # 断言叫assert,断言是框架提供的,要想调用断言,那么必须加上self.因为测试用例类继承了框架中的TestCase类,
        # 也继承了这个类中断言,所以我们可以直接用断言中的方法
        # 断言有几个特点:
        # 1.断言比较简洁
        # 2.断言关注于错误的测试用例,只有断言出错的时候,才会打印信息,正确是没有任何的信息提示
        # 3.断言报错时后边的代码将不会继续执行,前面的步骤失败了,后边的步骤就不需要继续尝试执行了
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main