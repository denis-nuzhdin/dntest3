# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)
main_page = "http://demo07.i-sys.ru:3003/"
username = "i-sys\dt-tst-1"
password = "PassW0rd"

def open_start_page():
    wd.get(main_page)
    wd.find_element_by_id("username").click()
    wd.find_element_by_id("username").send_keys(username)
    wd.find_element_by_id("password").click()
    wd.find_element_by_id("password").send_keys(password)
    wd.find_element_by_id("SubmitCreds").click()


try:
    open_start_page()
    wd.find_element_by_xpath(".//li[contains(*,'Журналы регистрации')]//a[contains(span,'Входящие')]").click()
    wd.find_element_by_xpath(".//*[@id='idHomePageNewItem']/span[text()='Создайте элемент']").click()
    #переключение в iframe
    frame = wd.find_element_by_xpath(".//iframe[contains(@id,'DlgFrame')]")
    wd.switch_to.frame(frame)

    #Исходящий номер
    ReferenceNumber = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceNumberEditContainerBody')]")
    ReferenceNumber.send_keys("123")


    #поиск инпута по названию поля
    #$x(".//nobr[contains(.,'Исходящий номер')]//ancestor::tr[1]//input")




finally:

    if not success:
        raise Exception("Test failed.")
