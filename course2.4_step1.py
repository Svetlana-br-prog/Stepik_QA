from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
import pyperclip


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.execute_script("window.scrollBy(0, 130);")  # скролим страницу

    # говорим Selenium проверять в течение 12 секунд, пока цена не упадет до 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book").click()

    # счтаем пример
    browser.find_element_by_id("answer").send_keys (
        str(math.log(abs(12 * math.sin(int(browser.find_element_by_id("input_value").text)))))
    )
    browser.find_element_by_id("solve").click()

    # Копирование числа из алерта в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()