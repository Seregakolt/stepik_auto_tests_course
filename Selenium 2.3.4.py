from selenium import webdriver
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_tag_name("button").click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12 * math.sin(x)), math.e)))
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(8)
    browser.close()
