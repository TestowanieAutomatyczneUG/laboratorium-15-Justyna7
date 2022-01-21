import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path='D:/uczelnia/II rok/semestr 3/testowanie_automatyczne/lab15/laboratorium-15-Justyna7/zad1/chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://duckduckgo.com/")
        # driver.find_element()
        # time.sleep(5)
        driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        time.sleep(5)
        driver.find_element_by_id("search_button_homepage").submit()
        time.sleep(5)
        self.assertEqual(driver.title, "Selenium at DuckDuckGo")
        driver.quit()


if __name__ == '__main__':
    unittest.main()