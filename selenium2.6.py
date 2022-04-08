from selenium import webdriver
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x = int(browser.find_element_by_id("input_value").text)
    inp = math.log(abs(12 * math.sin(x)), math.e)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("answer").send_keys(str(inp))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(8)
    browser.close()
