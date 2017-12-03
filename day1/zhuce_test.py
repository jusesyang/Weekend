
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("注册").click()
# 浏览器窗口最大化
driver.maximize_window()
# 输入用户名
driver.find_element_by_name("username").send_keys("yangjun2")
# 输入密码
driver.find_element_by_name("password").send_keys("888888")
# 确认密码
driver.find_element_by_name("userpassword2").send_keys("888888")
# 输入手机号
driver.find_element_by_name("mobile_phone").send_keys("13112345679")
# 输入邮箱
driver.find_element_by_name("email").send_keys("1223@qq.com")
# 点击注册按钮
driver.find_element_by_class_name("reg_btn").click()

# 窗口切换:把selenium切换到新的窗口工作
# driver.current_window_handle 浏览器当前窗口的句柄
cwh=driver.current_window_handle
print(cwh)
# selenium只提供了selenium工作窗口的名字,并没有提供第二个窗口的名字,我们得自己求
whs = driver.window_handles#浏览器中所有的窗口句柄
for item in whs:

# 关闭浏览器
driver.close()



