import pytest
from selenium import webdriver
from AuthShopPage import AuthShopPage
from MainShopPage import MainShopPage
from CartShopPage import CartShopPage
from OrderShopPage import OrderShopPage
import allure


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description("Проверки: 1. Добавление товаров в корзину;"
                    "2. Соответствие товаров в корзине добавленным;"
                    "3. Рассчет итоговой стоимости корзины.")
@allure.feature("Интернет-магазин")
@allure.severity("Critical")
def test_shop(driver):
    auth_shop_page = AuthShopPage(driver)
    main_shop_page = MainShopPage(driver)
    cart_shop_page = CartShopPage(driver)
    order_shop_page = OrderShopPage(driver)

    auth_shop_page.open()
    auth_shop_page.auth("standard_user", "secret_sauce")
    main_shop_page.add_prod("sauce-labs-backpack")
    main_shop_page.add_prod("sauce-labs-bolt-t-shirt")
    main_shop_page.add_prod("sauce-labs-onesie")
    main_shop_page.click_cart()
    cart_shop_page.check_prods()
    order_shop_page.enter_info("Иван", "Наряднов", "400094")
    total = order_shop_page.check_total()
    driver.quit()
    with allure.step("Проверить фактический результат,"
                     "сравнив его с ожидаемым"):
        assert total == "$58.29"
