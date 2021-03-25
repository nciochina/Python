from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ciochina")
    input2 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/div[2]/input[1]")
    input2.send_keys("Nicu")
    input3 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/div[3]/input[1]")
    input3.send_keys("nciochina@afi.at")
    input4 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[2]/div[1]/input[1]")
    input4.send_keys("+37369120904")
    input5 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[2]/div[2]/input[1]")
    input4.send_keys("Calea Iesilor")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
    time.sleep(3)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()

