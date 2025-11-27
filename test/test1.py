from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com")

element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "A/B Testing"))).is_displayed()

print(element)
