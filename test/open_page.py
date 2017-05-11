# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import datetime
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)
main_page = "http://demo07.i-sys.ru:3003/"
username = "i-sys\dt-tst-1"
password = "PassW0rd"
curent_date = datetime.datetime.now().strftime("%d.%m.%Y")



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
    ReferenceNumber = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceNumber')]")
    ReferenceNumber.send_keys("123")

    #Исходящая дата
    ReferenceDate = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceDate')]")
    ReferenceDate.send_keys(curent_date)

    #Организация отправителя
    Organization = wd.find_element_by_xpath(".//td/div[contains(@id,'Organization')]")
    Organization.send_keys('ОАО "Энергия"')
    Organization.send_keys(Keys.RETURN)

    #Краткое содержание
    Summary = wd.find_element_by_xpath(".//textarea[contains(@id,'Summary')]")
    Summary.send_keys("многострочный текст")

    #Адресаты
    Addressee = wd.find_element_by_xpath(".//td/div[contains(@id,'Addressee')]")
    Addressee.send_keys("dt-tst-1")
    Addressee.send_keys(Keys.RETURN)



    #Срочно
    Urgently = wd.find_element_by_xpath(".//input[contains(@id,'Urgently')]")
    Urgently.click()


    #поиск инпута по названию поля
    #$x(".//nobr[contains(.,'Исходящий номер')]//ancestor::tr[1]//input")




finally:

    if not success:
        raise Exception("Test failed.")
