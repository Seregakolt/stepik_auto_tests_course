from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_css_selector("input[name='firstname']").send_keys("Sergey")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("Kolotov")
    browser.find_element_by_css_selector("input[name='email']").send_keys("kolt@mail.ru")
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(8)
    browser.close()
