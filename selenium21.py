from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    el1 = browser.find_element_by_id("robotCheckbox")
    el1.click()
    el1 = browser.find_element_by_id("robotsRule")
    el1.click()
    el1 = browser.find_element_by_tag_name("button")
    el1.click()
finally:
    time.sleep(10)
    browser.close()
