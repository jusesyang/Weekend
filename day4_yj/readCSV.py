# 要读CSV文件首先要准备一个csv文件
# 1.导入CSV的包,是python内置的包
import csv

# 2.要想读取这个文件需要知道这个文件的位置
# 字符串前边加一个字符r,表示反斜杠是普通字符,不看做转义字符
path =r"C:\Users\51Testing\PycharmProjects\Weekend\data\member_info.csv"

# 3.要想读文件的内容需要通过路径打开文件
file = open(path,'r')
# 4.通过csv代码库读取csv格式的内容
data_table=csv.reader(file)
# 5.遍历data_table,分别打印每一行数据
print(data_table)

for row in data_table:
    print(row)