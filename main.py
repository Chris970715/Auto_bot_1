from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from theGameBot import TheGameBot
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_driver_path = "C:\python_bot\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(options=options, service=service)


game_on = True

bot_0 = TheGameBot()
bot_0.connection(url = "http://orteil.dashnet.org/experiments/cookie/")
bot_0.target_cookie()


while(game_on):
    bot_0.target_cookie()
    bot_0.click()
    bot_0.buy_options()