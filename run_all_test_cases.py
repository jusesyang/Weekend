import unittest


if __name__ == '__main__':
    # 默认的测试用例加载器
    # discover
    suite=unittest.defaultTestLoader.discover("./day5", pattern='*Test.py')
#    执行suite中的所有的测试用例
#     TextTestRunner     #文本的 测试用例运行器
#     TextTestRunner  首字母大写说明他是一个类,类不能直接调用方法,需要先实例化成对象才能调用
#     python中的实例化不需要new关键字,直接在后边加一对括号
    unittest.TextTestRunner().run(suite)



