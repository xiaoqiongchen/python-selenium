from  selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class Common(object):
    driver=""
    def open_browser(self,browser_name):#启动浏览器驱动
        global driver
        if browser_name.lower().strip()=="ie":
           driver=webdriver.Ie()
        elif browser_name.lower().strip()=="firefox":
           driver=webdriver.Firefox()
        elif browser_name.lower().strip()=="chrome":
           driver=webdriver.Chrome()
        else:
            return ("未知浏览器")
        driver.maximize_window()

    def visit_url(self,url):#获取网页源码
        global driver
        driver.set_page_load_timeout(3)
        driver.get(url)

    def implicit_waiting(self,times):#隐式等待时间
        global driver
        driver.implicitly_wait(int(times))

    def sleep_time(self,times):
        time.sleep(int(times))

    def quit(self):#关闭网页
        global driver
        driver.quit()

    def location_element(self,type,element):#元素定位
        global driver
        if type.lower().strip()=="id":
          el= driver.find_element_by_id(element)
        elif type.lower().strip()=="name":
          el= driver.find_element_by_name(element)
        elif type.lower().strip()=="tag":
          el= driver.find_element_by_tag_name(element)
        elif type.lower().strip()=="class":
          el= driver.find_element_by_class_name(element)
        elif type.lower().strip()=="link_text":
          el= driver.find_element_by_link_text(element)
        elif type.lower().strip()=="partial_link":
          el= driver.find_element_by_partial_link(element)
        elif type.lower().strip()=="xpath":
          el= driver.find_element_by_xpath(element)
        elif type == "css_selector":
          el=  driver.find_element_by_css_selector(element)
        return el

    def input_content(self,type,element,data):#输入数据
        el=self.location_element(type,element)
        el.clear()
        return el.send_keys(data)

    def swith_to_iframe(self,type,element):#切至iframe
        global driver
        el=self.location_element(type,element)
        return driver.switch_to.frame(el)

    def swith_out_iframe(self):#切出iframe
        global driver
        return driver.switch_to.default_content()

    def click(self,type,element):#点击事件
        el=self.location_element(type,element)
        el.click()
    def submit(self,type,element):#表单提交事件
        el=self.location_element(type,element)
        el.submit()

    def keys_enter(self,type,element):#键盘回车事件
        el=self.location_element(type,element)
        el.send_keys(Keys.ENTER)

    def action_chains(self,type,element):#鼠标双击事件
        global driver
        el=self.location_element(type,element)
        action_chains = ActionChains(driver)
        action_chains.double_click(el).perform()







