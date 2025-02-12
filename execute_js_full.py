from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем нужную веб страницу
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/execute_script.html'
    browser.get(link)

    x = browser.find_element(By.XPATH, "//span[@id='input_value']")
    y = calc(x.text)

    text_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    text_field.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    # Прокручиваем страницу так, чтобы кнопка стала видимой
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Выполняем JavaScript-код для прокрутки страницы

    robot_checkbox = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
    robot_checkbox.click()

    robots_Rule = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    robots_Rule.click()

    button.click()

finally:
    time.sleep(20)
    browser.quit()