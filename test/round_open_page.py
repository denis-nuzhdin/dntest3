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
        sum = 1
        wd = self.wd
        total = 0
        summ_list = []

        for url in pages:
            for u in range(loops):
                self.wd.get(url)
                # time.sleep(3) # ждем 3 сек загрузку страницы, раскомментировать для Chrome!
                # получаем число миллисекунд для браузерного события onload
                stext = self.wd.execute_script(
                    "return ( window.performance.timing.domComplete - window.performance.timing.responseStart )")
                summ_list.append(stext)
                print ("url: " + url)
                print(stext)
                print(summ_list)

            sum_all = sum(summ_list)
            #average = sum_all / loops
            #print(average)
            print(sum_all)
            summ_list.clear()


            #total = total + int(stext)
            #print(total)




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


