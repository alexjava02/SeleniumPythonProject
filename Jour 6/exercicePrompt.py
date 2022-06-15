import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 1) Ouvrir la page avec le bon url
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

# 2) Cliquez sur le boutton "Click for JS Prompt"
driver.find_element(By.XPATH, "//button[contains(text(),'Prompt')]").click()
time.sleep(2)

# 3) Écrire du texte dans le prompt
promptWindow = driver.switch_to.alert
promptWindow.send_keys("Bonjour Rabah, voici l'exercice sur le prompt")
time.sleep(2)
print(promptWindow.text)
time.sleep(2)

# 4) Cliquez sur Ok
promptWindow.accept()
print(driver.find_element(By.ID, "result").text)

# 5) Quittez le programme
time.sleep(3)
driver.quit()