from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def enter_info(self, name, surname, index):
        self.driver.find_element(By.ID, "first-name").send_keys(name)
        self.driver.find_element(By.ID, "last-name").send_keys(surname)
        self.driver.find_element(By.ID, "postal-code").send_keys(index)
        self.driver.find_element(By.ID, "continue").click()
        self.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, "body")))

    def check_total(self):
        tot = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        total = tot.split("Total: ")[1]
        return total
