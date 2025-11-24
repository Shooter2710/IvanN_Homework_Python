from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

inputs = driver.find_element(By.CSS_SELECTOR, "[type='number']")
inputs.send_keys("Sky")
inputs.clear()
inputs.send_keys("Pro")
driver.quit()
