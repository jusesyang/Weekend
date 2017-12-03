
from selenium import webdriver
# 1.打开浏览器
driver = webdriver.Chrome()
driver.get("http://localhost/")
# 2.点击登录连接
driver.find_element_by_link_text("登录").click()
# 从浏览器中的所有窗口中,排除第一个窗口 把selenium 切换到第二个窗口
cwh = driver.current_window_handle
whs = driver.window_handles

for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to_window(item) #切换到item窗口

# 3.输入用户名密码
driver.find_element_by_id("username").send_keys("yangyang1")
# 4.点击登录按钮