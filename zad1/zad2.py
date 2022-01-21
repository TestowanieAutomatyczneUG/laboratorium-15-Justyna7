import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


#  zamiast click() dlaelementów formularza można użyć submit().
#  Ta funcja jest już niedostępna w selenium 4, gdzie można używać tylko click()

#  gdy selenium nie znajdzie szukanego elementu, zwróci selenium.common.exceptions.NoSuchElementException

class MyTestCase(unittest.TestCase):  # testujemy duckduckgo
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:/uczelnia/II rok/semestr 3/testowanie_automatyczne/lab15/laboratorium-15-Justyna7/zad1/chromedriver')

    def test_pierwszy(self):  # by_id
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        time.sleep(5)
        self.assertEqual(self.driver.title, "Selenium")
        self.driver.close()

    def test_trzeci(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-2").click()
        time.sleep(5)
        self.assertEqual(self.driver.title, "Selenium - Health Professional Fact Sheet")
        #self.assertEqual(self.driver.title, "Selenium - Wikipedia")
        self.driver.close()

    def test_classname(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        self.driver.find_element(By.CLASS_NAME, "selenium-button").click()
        time.sleep(5)
        self.assertEqual(self.driver.title, "WebDriver | Selenium")
        self.driver.close()

    def test_tagname(self):  # tagname
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        e = self.driver.find_elements(By.TAG_NAME, "section")
        time.sleep(5)
        self.assertEqual(len(e), 2)
        self.driver.close()

    def test_namer(self):  # name
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        self.driver.find_element_by_id("search_button_homepage").submit()
        self.driver.find_element_by_id("r1-0").click()
        val = self.driver.find_element(By.NAME, "generator").get_attribute("content")
        time.sleep(5)
        self.assertEqual(val, "Hugo 0.83.1")
        self.driver.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()