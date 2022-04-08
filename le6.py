from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Сергей")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Колотов")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Барабинск")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    but = browser.find_elements_by_xpath("//button[text()='Submit']")[0]
    but.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()