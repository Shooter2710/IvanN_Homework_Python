from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# ВАРИАНТ 1. НЕЯВНОЕ ОЖИДАНИЕ:

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

driver.implicitly_wait(16)

greenLine = driver.find_element(By.CLASS_NAME, "bg-success").text

print("Неявное ожидание - ", greenLine)

# ВАРИАНТ 2. ЯВНОЕ ОЖИДАНИЕ:

driver.refresh()

driver.find_element(By.ID, "ajaxButton").click()

greenLine = WebDriverWait(driver, 16).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    ).text

print("Явное ожидание - ", greenLine)

driver.quit()
