
from selenium import webdriver
import time
# import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

# 5.商品图册
driver.find_element_by_link_text("商品图册").click()
# 有些页面控件是javascript在页面加载之后生成的,implicitly_wait()是用来判断整个网页是否加载完毕
# 有些页面加载完,但是javascript的控件还没有创建好,所以需要加一个time.sleep()提高程序的稳定性
time.sleep(3)
# ActionChains(driver).move_to_element(driver.find_element_by_class_name("webuploader-pick")).click().perform()
# js='document.getElementsByTagName("input")[17].setAttribute("class","")'
# driver.execute_script(js)
# photo_path=os.path.abspath('item1.png')
# driver.get(photo_path)
# js='document.getElementsByTagName("input")[17].setAttribute("class","")'
# driver.execute_script(js)
driver.find_element_by_name("file").send_keys("D:/item1.png")
# driver.find_element_by_name("file").submit()

# 因为真正负责上传文件的页面元素是<input type='file'...,所以我们可以直接操作这个控件
# 这个控件可以直接输入图片的路径

driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
time.sleep(3)
driver.switch_to.alert.accept()  #alert控件不是立刻就弹出来的需要时间等待

driver.find_element_by_class_name("button_search").click()
#
ac =ActionChains(driver)
for item in range(10):
    ac.send_keys(Keys.ARROW_DOWN)
ac.perform()

# driver.execute_script("window.scrollTO(200.100)") 向右200像素 向下100像素






