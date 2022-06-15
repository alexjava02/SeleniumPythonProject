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
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window() #permet d'ouvrir la fenêtre au maximum lors de l'exécution
# 3) Entrer username (Admin)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "btnLogin").click()
# 6) recuperer le titre de la page(titre actuel)
act_title =  driver.title
exp_title = "OrangeHRM"
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
if act_title == exp_title:
    print("Le test Login est passed")
else:
    print("Le test Login est failed")
time.sleep(4)
# 8) Fermer le navigateur
driver.close()