from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Ввести свои имя, фамилию и индекс: {name}, {surname},"
                 "{index} и нажать кнопку 'Continue'")
    def enter_info(self, name: str, surname: str, index: str):
        """Функция заполняет поля 'First name', 'Last name', 'Zip/Postal Code'
        выбранными данными и нажимает кнопку 'Continue'"""
        self.driver.find_element(By.ID, "first-name").send_keys(name)
        self.driver.find_element(By.ID, "last-name").send_keys(surname)
        self.driver.find_element(By.ID, "postal-code").send_keys(index)
        self.driver.find_element(By.ID, "continue").click()
        self.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, "body")))

    @allure.step("Определить значение фактической суммы 'Total' для проверки")
    def check_total(self) -> str:
        """Функция возвращает значение итоговой суммы 'Total'"""
        tot = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        total = tot.split("Total: ")[1]
        return total
