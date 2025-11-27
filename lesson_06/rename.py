from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")

driver.find_element(By.ID, "updatingButton").click()

renameButton = driver.find_element(By.ID, "updatingButton").text

print(renameButton)

driver.quit()
