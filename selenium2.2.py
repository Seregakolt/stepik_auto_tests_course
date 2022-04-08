from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    n1 = browser.find_element_by_id("num1").text
    n2 = browser.find_element_by_id("num2").text
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value='{int(n1) + int(n2)}']").click()
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.close()
