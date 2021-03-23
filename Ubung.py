from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://suninjuly.github.io/simple_form_find_task.html")
button = driver.find_elements_by_id("submit_button")

button.click()

driver.quit()