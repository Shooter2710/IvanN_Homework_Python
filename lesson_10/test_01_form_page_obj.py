import pytest
from selenium import webdriver
from FormPage import FormPage
import allure


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование формы")
@allure.description("Проверка состояния полей формы после заполнения")
@allure.feature("Форма")
@allure.severity("Minor")
def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    with allure.step("Проверить состояние всех полей"):
        form_page.check_form_submission()
