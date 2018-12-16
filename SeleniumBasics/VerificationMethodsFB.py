from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(20)
Value = driver.find_element(By.XPATH, "//label[text()='Female']").is_selected()
print(Value)