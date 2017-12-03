from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost/")
# 点击注册连接
driver.find_element_by_link_text("注册").click()

# 窗口切换:把selenium切换到新的窗口工作
# driver.current_window_handle 浏览器当前窗口的句柄
cwh = driver.current_window_handle
print(cwh)
# selenium只提供了selenium工作窗口的名字,并没有提供第二个窗口的名字,我们得自己求
whs = driver.window_handles  # 浏览器中所有的窗口句柄
'''
item表示whs中的一个元素,每次循环取一个值,循环结束,whs中的每个元素都会被遍历一次
python语法:遇到冒号下一行要空4个空格
'''
print(whs)

for item in whs:
    if item == cwh:
        driver.close()  # 关闭当前浏览器标签
    else:  # 这种情况,item就是我们要找的窗口了
        driver.switch_to_window(item)

# 输入用户信息
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
