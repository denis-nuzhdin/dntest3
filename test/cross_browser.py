# -*- coding: utf-8 -*-
#from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from selenium import webdriver


#wd = webdriver.Chrome('/usr/local/bin/chromedriver')
#wd = webdriver.Firefox()
wd = webdriver.Ie('C:\Python35-32\IEDriverServer.exe')

main_page = "http://google.com"

class test_add_element(unittest.TestCase):
    def setUp(self):
        self.wd = wd
        self.wd.implicitly_wait(10)

    def test_open_main_page(self):
        wd = self.wd
        wd.get(main_page)

