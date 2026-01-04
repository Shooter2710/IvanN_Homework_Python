import pytest
from selenium import webdriver
from CalcPage import CalcPage
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Проверки: 1. Функциональность таймера ожидания"
                    "ответа калькулятора; 2. Видимость ответа на дисплее;"
                    "3. Соответствие фактического ответа ожидаемому.")
@allure.feature("Калькулятор")
@allure.severity("Critical")
def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()

    calc_page.enter_wait_value('45')

    calc_page.press_calc_button('7')
    calc_page.press_calc_button('+')
    calc_page.press_calc_button('8')
    calc_page.press_calc_button('=')
    calc_page.expected_result('15')

    with allure.step("Проверить фактический результат,"
                     "сравнив его с ожидаемым"):
        assert calc_page.get_result() == calc_page.value
    driver.quit()
