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
    wd.find_element_by_xpath(".//li[contains(*,'Журналы регистрации')]//a[contains(span,'Входящие')]").click()
    #$x(".//li[contains(*,'Журналы регистрации')]//a[contains(span,'Входящие')]")
    wd.find_element_by_xpath(".//*[@id='idHomePageNewItem']/span[text()='Создайте элемент']").click()
    #переключение в iframe
    frame = wd.find_element_by_xpath(".//iframe[contains(@id,'DlgFrame')]")
    wd.switch_to.frame(frame)
    #Исходящий номер
    ReferenceNumber = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceNumberEditContainerBody')]")
    ReferenceNumber.send_keys("123")

    #поиск инпута по названию поля
    #$x(".//nobr[contains(.,'Исходящий номер')]//ancestor::tr[1]//input")


    #wd.switch_to.frame(wd.find_element_by_xpath(".//input[contains(@id,'ReferenceNumberEditContainerBody')]"))
    #element = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceNumberEditContainerBody')]").click()
    #element.send_keys("123")

finally:

    if not success:
        raise Exception("Test failed.")
