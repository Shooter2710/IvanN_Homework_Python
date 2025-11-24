from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver.get("https://google.com")

find=driver.find_element(By.ID, "APjFqb")
find.send_keys("Selenium")
find.send_keys(Keys.RETURN)

sleep(5)