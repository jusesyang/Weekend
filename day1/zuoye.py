
from selenium import webdriver
import time


# 1.打开浏览器
driver = webdriver.Chrome()
driver.get("http://localhost/")

js='document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)

# 2.点击登录连接
driver.find_element_by_link_text("登录").click()

driver.find_element_by_id("username").send_keys("shiji")

driver.find_element_by_id("password").send_keys("888888")

driver.find_element_by_class_name("login_btn").click()
time.sleep(3)
# 点击进入商城购物
driver.find_element_by_link_text("进入商城购物").click()
# 搜索框中输入
driver.find_element_by_class_name("input_ss").send_keys("iphone")
# 点击搜索按钮
driver.find_element_by_class_name("btn1").click()

js_img ='document.getElementsByClassName("shop_01-imgbox")[0].childNodes[1].setAttribute("target","")'
driver.execute_script(js_img)



item_img_css = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
driver.find_element_by_css_selector(item_img_css).click()
# time.sleep(8)
driver.implicitly_wait(5)
# cwh = driver.current_window_handle
# whs = driver.window_handles
#
# for item in whs:
#     if item == cwh:
#         driver.close()
#     else:
#         driver.switch_to_window(item)



driver.find_element_by_id("joinCarButton").click()
# time.sleep(5)
driver.implicitly_wait(10)
driver.find_element_by_class_name("shopCar_T_span3").click()
# driver.find_element_by_xpath('//*[@id="joinCarButton"]').click()



