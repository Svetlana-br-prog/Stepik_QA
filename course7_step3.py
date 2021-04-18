from selenium import webdriver
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 130);") # скролим страницу

    def cals(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    number_list = browser.find_element_by_id("input_value")
    x = number_list.text
    y = cals(x)

    # Ввести в поле ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Ставим галочку в checkbox
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Ставим галочку в  radiobuttons
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Нажать кнопочку
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()