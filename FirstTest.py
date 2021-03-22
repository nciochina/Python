from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bnm.md/")
driver.maximize_window()
element = driver.find_element_by_xpath("//a[contains(text(),'Media')]")
element.click()

