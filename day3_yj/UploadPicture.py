from selenium import webdriver
import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
login_url="http://localhost/index.php?&m=admin&c=public&a=login"
driver.get(login_url)
user_name="admin"
user_pwd="password"
verify_no="1234"
# 1.登录
driver.find_element_by_name("username").send_keys(user_name)
driver.find_element_by_name("userpass").send_keys(user_pwd)
driver.find_element_by_name("userverify").send_keys(verify_no)
driver.find_element_by_class_name("Btn").click()

# 2.商品管理

driver.find_element_by_link_text("商品管理").click()
# 3.添加商品
driver.find_element_by_link_text("添加商品").click()
# 4.商品名称
driver.switch_to.frame("mainFrame") #切换到子框架 name=mainFrame
driver.find_element_by_name("name").send_keys("iphone9")
driver.find_element_by_css_selector("[id='1']").click()
# driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
driver.find_element_by_id("7").click()
# driver.find_element_by_id("jiafen").click()
# 双击是一种特殊的元素操作,被封装到ActionChains这个类中
# Java封装到Actions这个类中
# 链表必须以perform方法作为结尾
# 可以执行一组操作,只要最后以perform()结束就可以了

ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()



# 6.商品品牌
# brand = driver.find_element_by_name("brand_id")
# Select(brand).select_by_value("1")
brand1 = driver.find_elements_by_tag_name("select")[0]
Select(brand1).select_by_visible_text("苹果 (Apple)")

# 5.商品图册
driver.find_element_by_link_text("商品图册").click()
time.sleep(3)

# ActionChains(driver).move_to_element(driver.find_element_by_class_name("webuploader-pick")).click().perform()
# driver.find_element_by_css_selector("#filePicker label").click()

driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
time.sleep(3)
driver.switch_to.alert.accept()  #alert控件不是立刻就弹出来的需要时间等待

driver.find_element_by_class_name("button_search").click()