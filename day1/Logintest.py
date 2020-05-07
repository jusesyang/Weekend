# 打开浏览器


from selenium import webdriver

# 从selenium 中导入 webdriver 网络驱动 ,用代码来模拟浏览器的操作

driver = webdriver.Chrome()
driver.maximize_window()
# 打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")

# 输入用户名
driver.find_element_by_id("username").send_keys("yll")
# 输入密码
driver.find_element_by_id("password").send_keys("888888")
driver.find_element_by_class_name("login_btn").click()
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/ul/li[5]/input").click()
# 输入密码
# 点击登录按钮

