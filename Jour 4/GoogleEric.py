# Test Cases
# 1- importer selenium webdriver
# 2- créer une instance de chrome
# 3- aller sur google.com
# 4- saisir "selenium " dans la recherche
# 5- cliquer sur le choix prérenseigné à "selenium webdriver"
#
# -------------------------------------------------------------------------------
# 1- importer selenium webdriver
from datetime import time
import time

from selenium import webdriver
# 2- créer une instance de chrome
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
time.sleep(1)
# 3- aller sur google.com
driver.get("https://www.google.com")
time.sleep(1)
# 4- saisir selenium dans la recherche
driver.find_element(By.NAME, "q").send_keys("selenium ")
time.sleep(1)

driver.find_element(By.XPATH, "//span[. = 'selenium webdriver']").click()
time.sleep(3)
# Fermeture de la page
driver.quit()