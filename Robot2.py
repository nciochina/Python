from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
try:
   browser = webdriver.Chrome(ChromeDriverManager().install())
   browser.get("http://suninjuly.github.io/get_attribute.html")

   x_element = browser.find_element_by_xpath("//img[@id='treasure']")
   x = x_element.get_attribute("valuex")
   print(x)
   y = calc(x)

   input1 = browser.find_element_by_xpath("//input[@id='answer']")
   input1.send_keys(y)
   check = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
   check.click()
   radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
   radio.click()
   button = browser.find_element_by_css_selector("button.btn")
   button.click()

finally:
    time.sleep(5)
    browser.quit()

