import os
import smtplib
import unittest
# HTML.TestRunner是基于unittest框架的一个扩展,可以自己在网上下载
import sys
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path,"rb")
    mail_body = f.read()
    f.close()

    # 要想发邮件要把二进制转成MIME格式,MIME:multiple 多用途 I:internet互联网 M:mail 邮件 E:extension 扩展
    # 这种格式是对邮件协议的扩展,使邮件不仅支持文本,还支持多种格式,图片,音频,或者是二进制文件等
    msg = MIMEText(mail_body,'html','utf-8')
    # msg是字典
    msg['Subject']= Header("自动化测试报告",'utf-8')
#     如果想用客户端软件或者自己写代码登录邮箱,很多邮箱的服务器需要设置授权码,为了邮箱安全着想
    msg['From'] = "bwftest126@126.com"
    msg['To'] = "441934625@qq.com"

#     发邮件手动步骤
#     1.打开登录页面,即连接邮箱服务器,要想连接服务器,首先需要搞清楚网络传输协议
#     2.发邮件的协议一般有三种,要先知道邮箱支持哪种协议:pop3,smtp,imap
#     3.我们要选一种传输协议用来发邮件,smtp simple mail transport protocol
#     首先导入smtp代码库
    smtp = smtplib.SMTP() #实例化了一个smtp对象
    smtp.connect("smtp.126.com") #连接126邮箱的 服务器地址
#     2.登录邮箱
    smtp.login("bwftest126@126.com","abc123asd654")
#     3.发送邮件
    smtp.sendmail(msg['From'],msg['To'] , msg.as_string())
#     4.退出邮箱
    smtp.quit()
    print("email has sent out!")



if __name__ == '__main__':
    now_time = time.strftime("%Y-%m-%d_%H-%M-%S")

    suite=unittest.defaultTestLoader.discover("./day5","*Test.py")
    # unittest.TextTestRunner() 文本测试用例运行器
    # 现在用HTML的测试用例运行器
    # HTML测试用例运行器最后会生成一个html格式的测试报告,我们需要指定一下报告的路径

    # run_time=datetime.datetime.now()
    base_path=os.path.dirname(__file__)
    path = base_path +"/report/report"+now_time+".html"
    file = open(path,'wb')

    runner=HTMLTestRunner(stream=file,title="海盗商城测试报告",description="测试环境:windows server 2008 + Chrome 54")
    runner.run(suite)
    # 这时生成的测试报告,只显示类名和方法名,只能显示给专业的人士看
    # 我们应该把相关的手动测试用例的标题添加到我们的测试报告
    # 我们自动化测试用例是从手工测试用例中挑出来的,手工测试用例怎么写我们就怎么编写代码,我们需要把手工测试用例的标题写到代码里
    file.close()
    send_mail(path)