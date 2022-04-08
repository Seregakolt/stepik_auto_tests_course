from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element_by_id("button")
finally:
    time.sleep(8)
    browser.close()
