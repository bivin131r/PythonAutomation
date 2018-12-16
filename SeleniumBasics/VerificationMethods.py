from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///C:/Users/bivin/Desktop/Practise.html")
time.sleep(20)
Value = driver.find_element(By.ID, "Pythonradio").is_selected()
print(Value)