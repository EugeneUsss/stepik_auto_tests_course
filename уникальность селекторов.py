from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    input3.send_keys("I_petrov@mail.ru")

    input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.form-control.first")
    input4.send_keys("89154043565")

    input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.form-control.second")
    input5.send_keys("Москва")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла