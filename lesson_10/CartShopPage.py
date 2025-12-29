from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import allure


class CartShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_checkout(self):
        """Функция нажимает на кнопку 'Checkout'"""
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, "body")))

    @allure.step("Проверить товары в корзине на соответствие"
                 "добавленным и нажать на кнопку 'Checkout'")
    def check_prods(self):
        """Функция проверяет соответствие товаров в корзине товарам в файле"""
        with open('buy.csv') as file:
            reader = csv.reader(file)
            buy = list(reader)
        for prod in buy[0]:
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, f"remove-{prod}")))
        self.click_checkout()
