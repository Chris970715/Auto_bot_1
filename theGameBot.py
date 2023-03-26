from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class TheGameBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        chrome_driver_path = "C:\python_bot\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)

        self.driver = webdriver.Chrome(options=options, service=service)
        self.count = 0

    def connection(self, url):
        self.driver.get(url)

    def target_cookie(self):

        self.cookie = self.driver.find_element(By.ID,value="cookie")

    def click(self):
        self.money = self.driver.find_element(By.ID, value="money")
        self.cookie = self.driver.find_element(By.ID, value="cookie")
        self.cookie.click()

    def buy_options(self):
        self.money = self.driver.find_element(By.ID, value="money")
        self.store = self.driver.find_elements(By.CSS_SELECTOR, value="#store b")
        store_list = [(each.text).split(" - ")[1] for each in self.store if each.text != ""]

        for each in store_list[::-1]:
            check_0 = each.replace(',', '')
            check_1 = self.money.text.replace(',', '')
            if int(check_1) > int(check_0):
                check_2 = self.count + 7
                self.store[check_2].click()  # Wait for page content to update
                self.count = 0
                break
            self.count -= 1
        self.count = 0

