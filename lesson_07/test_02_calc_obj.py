import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()

    calc_page.enter_wait_value('45')

    calc_page.press_calc_button('7')
    calc_page.press_calc_button('+')
    calc_page.press_calc_button('8')
    calc_page.press_calc_button('=')
    calc_page.expected_result('15')

    assert calc_page.get_result() == calc_page.value
    driver.quit()
