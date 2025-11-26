from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://ya.ru")

driver.minimize_window()

sleep(5)

driver.maximize_window()

sleep(5)