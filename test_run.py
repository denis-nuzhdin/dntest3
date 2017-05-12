# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

class test_run(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)

    def open_page(self):
        wd = self.wd
        wd.get('http://www.google.com')

    def tearDown(self):
        self.wd.quit()

if __name__=='__main__':
    unittest.main()