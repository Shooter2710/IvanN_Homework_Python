from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


def test_color():
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7 985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.CLASS_NAME, "mt-3").click()

    zip_code = driver.find_element(By.ID, "zip-code"
                                   ).value_of_css_property("background-color")
    assert zip_code == "rgba(248, 215, 218, 1)"

    fields = ["first-name", "last-name", "address", "e-mail",
              "phone", "city", "country", "job-position", "company"]
    for field in fields:
        color = driver.find_element(By.ID, field
                                    ).value_of_css_property("background-color")
        assert color == "rgba(209, 231, 221, 1)"

    driver.quit()
