from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.LINK_TEXT,"Register").click()

driver.find_element(By.ID,"FirstName").send_keys("Alex essaie1")
driver.find_element(By.ID,"LastName").send_keys("Alex")
driver.find_element(By.ID,"Email").send_keys("Alex.com")
driver.find_element(By.ID,"Password").send_keys("allo")
driver.find_element(By.ID,"ConfirmPassword").send_keys("allo")

driver.find_element(By.ID,"register-button").submit()
driver.find_element(By.ID,"register-button").submit()




time.sleep(4)
driver.close()