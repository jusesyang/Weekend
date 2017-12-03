# javascript 是一门独立的语言
# 要想学号selenium,最重要的三件事:
'''
1.元素的定位:id-->name--->class
link_text 必须是连接,必须是<a>标签,必须得是文本
2.元素的操作:鼠标左键点击click,发送键盘上的案件 send_keys
3.学好javascript
 用javascript实现窗口切换

'''

from selenium import webdriver
import time
# 1.打开浏览器
driver = webdriver.Chrome()
driver.get("http://localhost/")


# javascript和python是不同的语言,pycharm是用来写python语言的
# 怎么在pycharm中执行javascript语言
js='document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')

# 2.点击登录连接
driver.find_element_by_link_text("登录").click()

driver.find_element_by_id("username").send_keys("yyyyy")

driver.find_element_by_id("password").send_keys("dsajfklsajf")
time.sleep(5)
d_xpath="/html/body/div[3]/div[2]/form/input"

#