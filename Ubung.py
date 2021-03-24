from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "https://www.bnm.md/"
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    driver.maximize_window()
    element = driver.find_element(By.XPATH, "//a[contains(text(),'Media')]")
    element.click()

finally:
    time.sleep(5)
    driver.quit()
