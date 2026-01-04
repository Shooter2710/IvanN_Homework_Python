from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AuthShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открыть сайт 'https://www.saucedemo.com'")
    def open(self):
        """Функция открывает сайт в браузере"""
        self.driver.get("https://saucedemo.com")

    @allure.step("Заполнить поля авторизации {login}:{password}"
                 "и нажать на кнопку 'Login'")
    def auth(self, login: str, password: str):
        """Функция вводит выбранные данные в поля 'Username',
        'Password'и нажимает кнопку 'Login'"""
        self.driver.find_element(By.ID, "user-name").send_keys(login)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        self.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, "body")))
