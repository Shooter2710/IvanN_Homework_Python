from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def auth(self, login, password):
        self.driver.find_element(By.ID, "user-name").send_keys(login)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        self.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, "body")))
