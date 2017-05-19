# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import datetime
import  random
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
#main_page = "https://test.uclholding.com:4433/Lists/ListOutcoming/AllItems.aspx"
username = "i-sys\dt-tst-1"
password = "PassW0rd"


curent_date = datetime.datetime.now().strftime("%d.%m.%Y")
delay_dynamic = time.sleep(2)

class test_add_element(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.mouse = ActionChains(self.wd)

    def test_open_create_element(self):
        wd = self.wd
        self.open_main_page(wd)


    def open_main_page(self, wd):
        wd.get(main_page)
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_id("SubmitCreds").click()

       # -------------
        loops = 5  # число переоткрытий страниц
        wd = self.wd
        total = 0
        # в случае, если сайт работает с куками, их нужно проставить,
        # напр., так:
        # self.driver.execute_script( "document.cookie='name=value'" )
        # есть еще идеологически правильный способ, но он у меня не срабатывал:
        # self.driver.add_cookie({'name':'value'})
        ListStext = []
        for j in range(loops):
            self.wd.get(main_page)
        # time.sleep(3) # ждем 3 сек загрузку страницы, раскомментировать для Chrome!
        # получаем число миллисекунд для браузерного события onload
            stext = self.wd.execute_script(
                "return ( window.performance.timing.domComplete - window.performance.timing.responseStart )")

            total = total + int(stext)
            print(stext)
        print(total)
        print(total / loops)


