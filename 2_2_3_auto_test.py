from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


def calc(num1, num2):
  return str(int(num1) + int(num2))
  # return str(math.log(abs(12*math.sin(int(x)))))


try: 

    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    y = calc(num1, num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y) 


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
