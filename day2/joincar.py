import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# 隐式等待,一经设置,对后边所有语句都有效果,所以在创建浏览器时设置一次就可以了
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost")
# 在点击登录按钮之前,我们需要先删除target属性
# 但是javascript定位方式比selenium麻烦
# 可以用javascript替换selenium定位方式
# 用arguments关键字,可以把元素定位作为一个参数,替换到javascript中
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')", login_link)
login_link.click()

driver.find_element_by_id("username").send_keys("yll")
driver.find_element_by_id("password").send_keys("888888")
driver.find_element_by_id("password").submit()  # 不建议使用
# submit()用于提交from表单,form是html中的一个元素
# form表单的任何子孙节点都可以调用submit()方法提交表单
# time.sleep(5)
# 应该使用隐式等待,会自动判断网页是否加载完毕,当加载完毕后立刻开始执行后续操作
# 我们应该设置一个最大时间不能让程序无限等待,一般时间是30秒

# 点击进入商城购物
driver.find_element_by_link_text("进入商城购物").click()

driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()

img_iphone = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
img_link = "div.shop_01-imgbox > a"
# img是标签名,>标签前面的是父节点,后面的是子节点
# 如果想在css中写class属性,那么前面需要加上.
# :nth-child(2),表示当前节点在家中排行老二
# 为什么我们要把css selector中的内容改的越短越好
# 涉及到越多的网页元素(节点),代码的可维护性,健壮性就越差,因为开发人员一旦修改页面时,修改了这些节点,那么元素就不能定位成功了
time.sleep(3)
iphone = driver.find_element_by_css_selector(img_link)
driver.execute_script("arguments[0].removeAttribute('target')", iphone)

driver.find_element_by_css_selector(img_link).click()
# 加入购物车按钮


time.sleep(5)
driver.find_element_by_id("joinCarButton").click()
# 去购物车结算
driver.find_element_by_class_name("shopCar_T_span3").click()

driver.find_element_by_link_text("结算").click()

driver.find_element_by_class_name("add-address").click()

driver.find_element_by_name("address[address_name]").send_keys("yang")
driver.find_element_by_name("address[mobile]").send_keys("18210571234")

# driver.find_element_by_css_selector('[value="230000"]').click()
# driver.find_element_by_css_selector('[value="230600"]').click()
# driver.find_element_by_css_selector('[value="230602"]').click()
sheng = driver.find_element_by_id("add-new-area-select")
# 下拉框是一种比较特殊的网页元素,selenium专门为下拉框提供了一种定位方式
# 需要把这个元素从WebElement类型装换成select类型
# Select 是selenium专门为我们创建的一个类,用于操作下拉框的
# Select这个类中封装了很多操作下拉框的方法
# city = driver.find_element_by_id("linkagesel_297509")
# area = driver.find_element_by_id("linkagesel_290095")
Select(sheng).select_by_value("230000")
# Select(city).select_by_value("230600")
# Select(area).select_by_value("230602")
shi=driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
qu = driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_visible_text("建华区")


driver.find_element_by_name("address[address]").send_keys("万达广场B座1203")

driver.find_element_by_name("address[zipcode]").send_keys("151400")

driver.find_element_by_class_name("aui_state_highlight").click()

# addr1='//*[@id="add-new-area-select"]/option[2]'
# driver.find_element_by_xpath(addr1).click()
# driver.find_element_by_id("linkagesel_302806").click()
# addr3='//*[@id="linkagesel_061142"]/option[4]'
# driver.find_element_by_xpath(addr3).click()

# 定位第二个下拉框
