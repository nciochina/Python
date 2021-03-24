from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/find_link_text")
driver.maximize_window()
element = driver.find_element_by_link_text("224592")
element.click()
