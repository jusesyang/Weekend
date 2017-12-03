
# 测试框架是干什么用的?
# 最主要的就是组织和执行测试用例
# 1.导入unitest框架
import unittest
# java 中的类和文件名的关系:类名和文件名一样
# python中的可以一样,但是推荐文件名首字母小写,类名首字母大写
# 2.继承unitest中的父类
# python中的继承直接用小括号表示
# TestCase是测试用例的意思,我们在UnitestDemo中编写测试用例
class Unitest_Demo(unittest.TestCase):
    # 3.重写父类中的方法setUp和tearDown方法
    # def是方法的关键字
    # setUp是创建的意思
    # 类似与手动测试中的预置条件
    def setUp(self):
        print("这个方法会在测试用例执行之前执行")

    def tearDown(self):
        print("这个方法将会在测试用例方法之后执行")
    #4.编写测试用例方法
    def test_login(self):
        print("登录测试用例")
        self.zhuce()
    # 只有以test开头命名的方法才是测试用的方法
    # 测试用例方法可以直接被运行,普通方法不能直接被运行,只有被调用才能被执行
    def zhuce(self):
        print("注册测试用例")

    def test_search(self):
        print("搜索测试用例")

#如果你直接执行这个文件那么就会执行下面的语句,否则你执行其他文件,import这个文件的时候,下面的语句就不会执行了
if __name__ == '__main__':
    # 执行当前文件中所有的unitest测试用例
    unittest.main()
    Unitest_Demo().zhuce()