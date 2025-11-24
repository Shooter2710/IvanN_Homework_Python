from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get("https://python.org")

driver.find_element(By.CLASS_NAME, "donate-button").click()

