from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import math

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/find_xpath_form")
    # result = browser.find_element_by_link_text("224592")
    # result.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
