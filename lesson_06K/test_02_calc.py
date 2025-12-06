from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
           "slow-calculator.html")


def test_calc():
    lead = driver.find_element(By.ID, "delay")
    lead.clear()
    lead.send_keys("45")
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    WebDriverWait(driver, 46).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "[style='display: none;']")))
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

    driver.quit()
