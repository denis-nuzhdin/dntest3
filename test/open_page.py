# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://demo07.i-sys.ru:3003/")
    wd.find_element_by_id("username").click()
    wd.find_element_by_id("username").send_keys("i-sys\dt-tst-1")
    wd.find_element_by_id("password").click()
    wd.find_element_by_id("password").send_keys("PassW0rd")
    wd.find_element_by_id("SubmitCreds").click()
    wd.find_element_by_xpath(".//*[@id='zz13_RootAspMenu']/li[3]/ul/li[1]/a/span/span").click()
    wd.find_element_by_xpath(".//*[@id='idHomePageNewItem']/span[text()='Создайте элемент']").click()
    wd.switch_to.frame(wd.find_element_by_xpath("..//input[contains(@id,'ReferenceNumberEditContainerBody')]").click())


finally:

    if not success:
        raise Exception("Test failed.")
