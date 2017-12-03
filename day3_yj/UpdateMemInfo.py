
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
# 打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 输入用户名
driver.find_element_by_id("username").send_keys("shiji")
# 输入密码
driver.find_element_by_id("password").send_keys("888888")
driver.find_element_by_class_name("login_btn").click()
time.sleep(3)
driver.find_element_by_link_text("账号设置").click()
css_person_info="div.chaozuo > ul > li:nth-child(2) > a"
driver.find_element_by_css_selector(css_person_info).click()
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("石基三")
# 修改个人信息,clear()用来清除元素中原本的内容
# js_sex='document.getElementsByName("sex")[1,2].id="xb1"'
# driver.execute_script(js_sex)
# driver.find_element_by_id("xb1").click()
# driver.find_element_by_css_selector('[value="1"]').click()
# css可以用多个属性组合定位一个元素,一个元素的多个属性之间不能有空格
driver.find_element_by_css_selector('#xb[value="1"]').click()
# js_date='document.getElementById("date").value="1980-12-08"'
# driver.execute_script(js_date)

#js_date= document.getElementById("date").removeAttribute("readonly")
# 用arguments改上边输入,用selenium的定位方式,定位元素之后,对元素执行javascript脚本,删除readonly属性
date=driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
date.clear()
date.send_keys("1980-11-21")

# 用selenium调用javascript一共有两个关键字:
# 1.arguments[0]:表示用python语言代替一部分javascript
# 好处是,有时selenium定位比较容易
# 2.return 把javascript的执行结果返回给python语言
# 好处是,有时,selenium定位不到的元素,可以用javascript定位到

# js_date2=driver.execute_script("return document.getElementById('date')")
# 这句话等于 date=driver.find_element_by_id("date")
# js_date2.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("1234567")
driver.find_element_by_class_name("btn4").click()

# 这种邮件检查不了的html代码的弹出框,叫做alert,有单独的方法来处理
# alert控件不是html代码生成的,所以implicitly_wait对这个控件不管用,需要用time.sleep()
time.sleep(3)
# 切换到alert方法,和切换窗口的方法类似
# alert弹出框,accept:接受,同意,确定,dismiss:拒绝,取消
driver.switch_to.alert.accept()
ac =ActionChains(driver)
for item in range(10):
    ac.send_keys(Keys.ARROW_DOWN)
ac.perform()

