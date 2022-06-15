#Test Case
#------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
# 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
# 8) Fermer le navigateur
from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\alexg\\OneDrive\\Documents\\École informatique\\3ième session\\Automatisation de test\\Chrome driver\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome(service=service_obj)
# 2) Naviguer vers l'url https://demo.nopcommerce.com/
driver.get("https://demo.nopcommerce.com/")
# Permet d'ouvrir la fenêtre au maximum lors de l'exécution
driver.maximize_window()
# 3) Permet de cliquer sur Register sur la page d'accueil pour se créer un compte
driver.find_element(By.LINK_TEXT,"Register").click()
# 4) Remplir les champs obligatoires
driver.find_element(By.ID,"FirstName").send_keys("Alex essaie1")
driver.find_element(By.ID,"LastName").send_keys("Alex")
driver.find_element(By.ID,"Email").send_keys("Alex1@gmail.com")
driver.find_element(By.ID,"Password").send_keys("allo1234")
driver.find_element(By.ID,"ConfirmPassword").send_keys("allo1234")
# 5) Cliquer sur le bouton submit
driver.find_element(By.ID,"register-button").submit()

driver.find_element(By.CLASS_NAME,"ico-login").submit()

time.sleep(4)
# 6) Fermer le navigateur
driver.close()