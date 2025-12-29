from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    @allure.step("Открыть сайт 'https://bonigarcia.dev/"
                 "selenium-webdriver-java/slow-calculator.html'")
    def open(self):
        """Функция открывает сайт в браузере"""
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить время ожидания {value} сек.")
    def enter_wait_value(self, value: str):
        """Функция устанавливает выбранное время
        задержки результата вычисления"""
        lead = self.driver.find_element(By.ID, "delay")
        lead.clear()
        lead.send_keys(value)

    @allure.step("Нажать на кнопку {value} калькулятора")
    def press_calc_button(self, value: str):
        """Функция нажимает на выбранную кнопку калькулятора"""
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    @allure.step("Ввести ожидаемый результат - {value}")
    def expected_result(self, value: str):
        """Функция создает переменную ожидаемого результата"""
        self.value = value

    def get_result(self) -> str:
        """Функция возвращает фактический результат"""
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), f"{self.value}"))
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return result
