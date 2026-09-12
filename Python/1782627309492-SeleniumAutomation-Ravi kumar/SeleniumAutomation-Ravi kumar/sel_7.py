from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com")
driver.maximize_window()

time.sleep(3)

# Search iPhones
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("iphones")

# Click search button
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

time.sleep(5)

# Extract product names
products = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")

print(str(len(products)) + " products found")

for product in products:
    print(product.text)

driver.quit()