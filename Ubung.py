from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "https://www.bnm.md/"
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    driver.maximize_window()
    element = driver.find_element(By.ID, 'tip-1')
    element_checked = element.get_attribute("f")
    print("value of element: ", element_checked)
    assert element_checked is None, "People radio is not selected by default"
    # element.click()

finally:
    time.sleep(5)
    driver.quit()
