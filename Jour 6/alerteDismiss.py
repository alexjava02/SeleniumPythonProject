import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
time.sleep(2)

confirmWindow = driver.switch_to.alert
print(confirmWindow.text)

# Permet de cliquez sur annuler
confirmWindow.dismiss()

time.sleep(3)
driver.quit()
