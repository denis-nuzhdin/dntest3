# author: ivn_cote
# MIT license
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time


class Test3(unittest.TestCase):
    def setUp(self):  # блок выполняется перед запуском тестов
        self.driver = webdriver.Firefox()  # указываем драйвер браузера, можно также указать webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)  # 10 сек в качестве максимального таймаута для выполнения методов
        self.base_url = "http://www.i-sys.ru"  # тестируемый сайт
        self.verificationErrors = []
        self.driver.get(self.base_url + "/")  # открываем конкретную страницу

    def test_stat(self):  # единственный тест для запуска
        loops = 2  # число переоткрытий страниц
        driver = self.driver
        total = 0
        # в случае, если сайт работает с куками, их нужно проставить,
        # напр., так:
        # self.driver.execute_script( "document.cookie='name=value'" )
        # есть еще идеологически правильный способ, но он у меня не срабатывал:
        # self.driver.add_cookie({'name':'value'})
        for j in range(loops):
            driver.refresh()
            # time.sleep(3) # ждем 3 сек загрузку страницы, раскомментировать для Chrome!
            # получаем число миллисекунд для браузерного события onload
            stext = self.driver.execute_script(
                "return ( window.performance.timing.loadEventEnd - window.performance.timing.navigationStart )")
            total = total + int(stext)
            print
            "Value is: %s" % stext
        print
        "TOTAL is: %s" % (total / loops)
        self.assertEqual("0",
                         total)  # сравнение никогда не выполняется, это единственный способ (который я нашел), чтобы скрипт выводил стандартный вывод в консоль

    def tearDown(self):  # блок выполняется после запуска тестов
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
