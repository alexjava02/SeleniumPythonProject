# Exercice Google
# -------------------------------------------------------------------------------
# 1) Faire les imports nécessaire
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 2) Créer une instance de chrome
driver = webdriver.Chrome()
time.sleep(1)
# 3) Aller sur google.com
driver.get("https://www.google.com")
time.sleep(1)
# 4) Saisir selenium dans la recherche
driver.find_element(By.NAME, "q").send_keys("selenium ")
time.sleep(1)
# 5) Chercher "Selenium webdriver" et cliquer dessus
driver.find_element(By.XPATH, "//span[. = 'selenium webdriver']").click()
time.sleep(3)
# Fermeture de la page
driver.quit()