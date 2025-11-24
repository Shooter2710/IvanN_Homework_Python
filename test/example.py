from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

driver.get("https://example.com")

element = driver.find_element(By.TAG_NAME, "h1").text

print(element)


# from selenium import webdriver

# driver = webdriver.Chrome()
driver.get("https://www.example.com")

print(f'Заголовок страницы: {driver.title}')

driver.quit()