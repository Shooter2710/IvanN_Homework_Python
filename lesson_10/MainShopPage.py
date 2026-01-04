from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import allure


class MainShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.buy = []

    @allure.step("Добавить товар {prod} в корзину")
    def add_prod(self, prod: str):
        """Функция добавляет выбранный товар в корзину и
        сохраняет информацию по товару в файл"""
        self.driver.find_element(By.ID, f"add-to-cart-{prod}").click()
        self.buy.append(prod)
        with open('buy.csv', mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.buy)

    @allure.step("Нажать на значок корзины")
    def click_cart(self):
        """Функция нажимает на значок корзины"""
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, "body")))
