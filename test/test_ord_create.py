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
username = "i-sys\dt-tst-1"
password = "PassW0rd"
curent_date = datetime.datetime.now().strftime("%d.%m.%Y")
delay_dynamic = time.sleep(2)

class test_add_element(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.mouse = ActionChains(self.wd)

    def delay_dyn(self):
        time.sleep(2)

    def test_open_create_element(self):
        wd = self.wd
        self.open_main_page(wd)
        self.open_ord_page(wd)
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

    def open_ord_page(self, wd):
        wd.find_element_by_xpath(".//li[contains(*,'Рабочие документы')]//a[contains(span,'ОРД')]").click()

    def open_form_new(self, wd):
        wd.find_element_by_xpath(".//*[@id='idHomePageNewItem']/span[text()='Создайте элемент']").click()

    def change_to_iframe(self, wd):
        frame = wd.find_element_by_xpath(".//iframe[contains(@id,'DlgFrame')]")
        wd.switch_to.frame(frame)

    def fill_form(self, wd):
        #Вид документа
        #DocViewOptions = wd.find_element_by_xpath(".//select[contains(@id,'DocView')]/option[text()='Политика']")
        #DocView = [wd.find_element_by_xpath(".//select[contains(@id,'DocView')]")]
        DocViewOptions = wd.find_elements_by_xpath(".//select[contains(@id,'DocView')]/option")
        DocViewOptionsList = []
        for option in DocViewOptions:
            DocViewOptionsList.append(option.get_attribute("text"))

        #for optionValue in DocViewOptionsList:
        #    print (optionValue)

        #DocViewOptionsRandomValue = random.choice(DocViewOptionsList)
        #print (DocViewOptionsRandomValue)
        #wd.find_element_by_xpath(".//select[contains(@id,'DocView')]/option[text()='"+DocViewOptionsRandomValue+"']").click()

        # -------------
        loops = 10  # число переоткрытий страниц
        wd = self.wd
        total = 0
        # в случае, если сайт работает с куками, их нужно проставить,
        # напр., так:
        # self.driver.execute_script( "document.cookie='name=value'" )
        # есть еще идеологически правильный способ, но он у меня не срабатывал:
        # self.driver.add_cookie({'name':'value'})
        ListStext = []
        for j in range(loops):
            DocViewOptionsRandomValue = random.choice(DocViewOptionsList)
            print(DocViewOptionsRandomValue)

            WebDriverWait(wd, 20).until(
            EC.element_to_be_clickable((By.XPATH, ".//select[contains(@id,'DocView')]")))
            wd.find_element_by_xpath(
                ".//select[contains(@id,'DocView')]/option[text()='" + DocViewOptionsRandomValue + "']").click()
        # time.sleep(3) # ждем 3 сек загрузку страницы, раскомментировать для Chrome!
        # получаем число миллисекунд для браузерного события onload
            stext = self.wd.execute_script(
                "return ( window.performance.timing.domComplete - window.performance.timing.responseStart )")

        for st in DocViewOptions:
            DocViewOptionsList.append(option.get_attribute("text"))

            total = total + int(stext)
            total2 = total + j
            print(stext)
        print(total)
        print(total2)
        print(total / loops)
        print(total2 / loops)




        #DocViewOptionsValue = wd.find_element_by_xpath(".//select[contains(@id,'DocView')]/option[text()="+ random 'Политика']")







        #wd.execute_script("return arguments[0].scrollIntoView();", DocViewOptions)

        #DocViewOptions.click()
        #self.delay_dyn()

        # Исходящая дата
        #ReferenceDate = wd.find_element_by_xpath(".//input[contains(@id,'ReferenceDate')]")
        #ReferenceDate.send_keys(curent_date)

        # Организация отправителя
        #Organization = wd.find_element_by_xpath(".//td/div[contains(@id,'Organization')]")
        #Organization.send_keys('ОАО "Энергия"')
        #Organization.send_keys(Keys.RETURN)
        #self.delay_dyn()

        # Краткое содержание
        #WebDriverWait(wd, 20).until(
        #EC.element_to_be_clickable((By.XPATH, ".//textarea[contains(@id,'Summary')]")))
        #Summary = wd.find_element_by_xpath(".//textarea[contains(@id,'Summary')]")
        #Summary.send_keys("многострочный текст")

        # Адресаты
        #Addressee = wd.find_element_by_xpath(".//td/div[contains(@id,'Addressee')]")
        #wd.execute_script("return arguments[0].scrollIntoView();", Addressee)
        #Addressee.send_keys("dt-tst-1")
        #Addressee.send_keys(Keys.RETURN)
        #self.delay_dyn()

        # Срочно
        #Urgently = wd.find_element_by_xpath(".//input[contains(@id,'Urgently')]")
        #wd.execute_script("return arguments[0].scrollIntoView();", Urgently)
        #Urgently.click()


    #def tearDown(self):  # блок выполняется после запуска тестов
        #self.wd.quit()
        #self.assertEqual([], self.verificationErrors)








