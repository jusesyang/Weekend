# 1.之前的readcsv不能被其他的测试用例调用,所以应该给他封装到一个方法中
# 2.每个测试用例的路径不同path应该作为参数传入到方法中
# 4.我们打开了文件但是没有关闭,最终可能造成内存泄露
import csv
import os


def read(filename):
    # 所有重复的代码出现,都是程序设计的不合理
    # 重复代码应该封装在一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/" + filename)
    # file = open(path,"r")
    # with语句是一个代码块,代码块中的内容都要缩进4个空格
    # with代码块可以自动关闭with中声明的变量
    # 因为file文件一旦被关闭,里面的数据也会随之消失,所以单独声明一个列表result,来保存里面的数据
    result = []
    with open(path,"r") as file:
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
    return result
    # 如果在打开和关闭程序的代码之间,发生了异常,导致后面的代码不能正常的运行,file.close()这时文件仍然不能关闭
    # 应该用with...as 关闭
    file.close()

# def get_result(row):
#     for row in result:
#         print(row)

if __name__ == '__main__':
    # path = r"C:\Users\51Testing\PycharmProjects\Weekend\path =r"C:\Users\51Testing\PycharmProjects\Weekend\data\member_info.csv""
    # 3.这个路径是一个绝对路径,工作中一个项目不止一个人编写代码,没法统一要求大家都把项目代码放在一个路径下
    # 这个文件因为在项目中所以他的路径也会随着项目变化
    # 所以应该在代码中,通过当前代码文件的路径,根据相对位置找到,找到csv文件
    # 所以首先要找到当前文件的路径
    # os是操作系统 path是路径,dir是directory目录
    # __file__是python内置的变量,指的是当前文件
    # print(current_file_path)
    # 我们真正想要的路径是csv文件的路径
    member_info=read("member_info.csv")
    for row in member_info:
        print(row)

    # 5.读出数据不是目的,目的是通过数据驱动测试,所以应该把数据作为方法的返回值方便进一步调用

    '''
    sadkjfaskljfklsjdfkljjas
    asdfkjsalkdjfkls
    jasdklfjksladjfjksjdfkj

    '''