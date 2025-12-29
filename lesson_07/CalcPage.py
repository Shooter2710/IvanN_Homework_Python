from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    def open(self):
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/slow-calculator.html")

    def enter_wait_value(self, value):
        lead = self.driver.find_element(By.ID, "delay")
        lead.clear()
        lead.send_keys(value)

    def press_calc_button(self, value):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def expected_result(self, value):
        self.value = value

    def get_result(self):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), f"{self.value}"))
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return result
