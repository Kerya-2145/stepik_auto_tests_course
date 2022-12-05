from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # link = "http://suninjuly.github.io/registration2.html"
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    """First test"""

    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class input')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class input')
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class input')
    email.send_keys("123@outlook.com")


    """Second test"""

    """
    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class input')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class input')
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class input')
    email.send_keys("123@outlook.com")

    phone = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.first_class input')
    phone.send_keys("123456789")
    address = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.second_class input')
    address.send_keys("all over the world")
    """

    

    """Third test"""
    """
    phone = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.first_class input')
    phone.send_keys("123456789")
    address = browser.find_element(By.CSS_SELECTOR, '.second_block .form-group.second_class input')
    address.send_keys("all over the world")
    """

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
