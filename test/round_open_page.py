# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import datetime
import random
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# wd = WebDriver()
main_page = "http://wikipedia.com/"
pages = ['http://wikipedia.com/'
    ,'http://yandex.com/'

]


class test_add_element(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.mouse = ActionChains(self.wd)

    def test_open_create_element(self):
        wd = self.wd
        self.open_main_page(wd)
        #print(pages)

    def open_main_page(self, wd):
        wd.get(main_page)

        # -------------
        loops = 2  # число переоткрытий страниц
        wd = self.wd
        total = 0

        for url in pages:
            for u in range(loops):
                self.wd.get(url)
                # time.sleep(3) # ждем 3 сек загрузку страницы, раскомментировать для Chrome!
                # получаем число миллисекунд для браузерного события onload
                stext = self.wd.execute_script(
                    "return ( window.performance.timing.domComplete - window.performance.timing.responseStart )")
                print(url)
                print(stext)
            total = total + int(stext)
            print(total)
            #print(url)




        #for j in range(loops):
        #    self.wd.get(main_page)
        #    # time.sleep(3) # ждем 3 сек загрузку страницы, раскомментировать для Chrome!
        #    # получаем число миллисекунд для браузерного события onload
        #    stext = self.wd.execute_script(
        #        "return ( window.performance.timing.domComplete - window.performance.timing.responseStart )")

        #   total = total + int(stext)
        #    print(stext)
        #print(total)
        #print(total / loops)


