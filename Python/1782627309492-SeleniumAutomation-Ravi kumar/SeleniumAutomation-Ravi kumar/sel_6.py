from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.amazon.in")

driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("iphones")

driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

time.sleep(5)

driver.quit()