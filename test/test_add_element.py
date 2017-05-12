# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import datetime
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time


#wd = WebDriver()
main_page = "http://demo07.i-sys.ru:3003/"
username = "i-sys\dt-tst-1"
password = "PassW0rd"
curent_date = datetime.datetime.now().strftime("%d.%m.%Y")

class test_add_element(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)

    def test_open_create_element(self):
        wd = self.wd
        self.open_main_page(wd)
        self.open_incoming_page(wd)
        self.open_form_new(wd)
        self.change_to_iframe(wd)
        self.fill_form(wd)

        #Сохранить и продолжить
        #SaveAndKeepEditing = wd.find_element_by_xpath(".//input[contains(@btncommand,'SaveAndKeepEditing')]")
        #SaveAndKeepEditing.click()

        #Зарегистрировать
        #Regestration = wd.find_element_by_xpath(".//input[contains(@value,'Зарегистрировать')]")
        #Regestration.click()

        #поиск инпута по названию поля
        #$x(".//nobr[contains(.,'Исходящий номер')]//ancestor::tr[1]//input")

    def open_main_page(self, wd):
        wd.get(main_page)
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_id("SubmitCreds").click()

    def open_incoming_page(self, wd):
        wd.find_element_by_xpath(".//li[contains(*,'Журналы регистрации')]//a[contains(span,'Входящие')]").click()

    def open_form_new(self, wd):
        wd.find_element_by_xpath(".//*[@id='idHomePageNewItem']/span[text()='Создайте элемент']").click()

    def change_to_iframe(self, wd):
        frame = wd.find_element_by_xpath(".//iframe[contains(@id,'DlgFrame')]")
        wd.switch_to.frame(frame)

    def fill_form(self, wd):
        # Исходящий номер
        ReferenceNumber = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceNumber')]")
        ReferenceNumber.send_keys("123")
        # Исходящая дата
        ReferenceDate = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceDate')]")
        ReferenceDate.send_keys(curent_date)
        # Организация отправителя
        Organization = wd.find_element_by_xpath(".//td/div[contains(@id,'Organization')]")
        Organization.send_keys('ОАО "Энергия"')
        Organization.send_keys(Keys.RETURN)
        # Краткое содержание
        # element = WebDriverWait(wd, 20).until(
        # EC.element_to_be_clickable((By.XPATH, ".//textarea[contains(@id,'Summary')]")))
        Summary = wd.find_element_by_xpath(".//textarea[contains(@id,'Summary')]")
        Summary.send_keys("многострочный текст")
        # Адресаты
        Addressee = wd.find_element_by_xpath(".//td/div[contains(@id,'Addressee')]")
        Addressee.send_keys("dt-tst-1")
        Addressee.send_keys(Keys.RETURN)
        # Срочно
        Urgently = wd.find_element_by_xpath(".//input[contains(@id,'Urgently')]")
        Urgently.click()










