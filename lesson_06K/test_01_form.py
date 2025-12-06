from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


def test_color():
    elem2 = driver.find_element(By.NAME, "first-name").send_keys("Иван")
    elem3 = driver.find_element(By.NAME, "last-name").send_keys("Петров")
    elem4 = driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    elem5 = driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    elem6 = driver.find_element(By.NAME, "phone").send_keys("+7 985899998787")
    elem7 = driver.find_element(By.NAME, "city").send_keys("Москва")
    elem8 = driver.find_element(By.NAME, "country").send_keys("Россия")
    elem9 = driver.find_element(By.NAME, "job-position").send_keys("QA")
    elem10 = driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.CLASS_NAME, "mt-3").click()

    elem1 = driver.find_element(By.ID, "zip-code"
                                ).value_of_css_property("background-color")
    assert elem1 == "rgba(248, 215, 218, 1)"

    elems = [elem2, elem3, elem4, elem5, elem6, elem7, elem8, elem9, elem10]
    for each in elems:
        color = driver.find_element(By.CLASS_NAME, "alert-success"
                                    ).value_of_css_property("background-color")
        assert color == "rgba(209, 231, 221, 1)"

    driver.quit()
