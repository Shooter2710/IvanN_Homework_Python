from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

driver.get("https://www.saucedemo.com/")


def test_shop():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "body")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "body")))

    driver.find_element(By.ID, "checkout").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "body")))

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Наряднов")
    driver.find_element(By.ID, "postal-code").send_keys("400094")
    driver.find_element(By.ID, "continue").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "body")))

    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    driver.quit()
    assert total == "Total: $58.29"
