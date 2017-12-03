# 1.首先导入pymysql代码库
import pymysql


def connDB():

# 我们想要连接数据库需要知道,数据库的:ip 端口号 用户名 密码 数据库名
    conn = pymysql.Connect(host="127.0.0.1", user="root", password="root",
                 database="pirate", port=3306,charset='utf8')
    sql = "select * from hd_user order by id desc"
    # 要想在代码中执行这段sql语句,首先需要获取数据库的游标Cursor
    curs = conn.cursor()
    # 通过游标执行sql语句
    curs.execute(sql)
    # 想获取数据库中最新的记录,就要用fetchone()
    result = curs.fetchone()

    return result


if __name__ == '__main__':
    data = connDB()
    print(data)