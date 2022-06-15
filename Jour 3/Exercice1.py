import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

# !!!!À NOTER J'AI MIT DES TIME.SLEEP POUR QU'ON VOIT BIEN LA DÉMARCHE D'ÉTAPE EN ÉTAPE LORS DE L'EXÉCUTION DU SCRIPT, JE SUIS CONSCIENT QUE DANS LA RÉALITÉ CE N'EST PAS NÉCESSAIRE

service_obj = Service("C:\\Users\\alexg\\OneDrive\\Documents\\École informatique\\3ième session\\Automatisation de test\\Chrome driver\\chromedriver.exe")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
driver = webdriver.Chrome(service=service_obj)
# 2) Naviguer vers l'url https://www.saucedemo.com/
driver.get("https://www.saucedemo.com/")
# Permet d'ouvrir la fenêtre au maximum lors de l'exécution
driver.maximize_window()
# 3) Permet de se connecter a swag labs
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
# 4) Mettre un article (Backpack) dans le panier
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
# 5) Aller dans le panier
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
# 6) Enlever l'élément qu'on vient d'ajouter du panier
driver.find_element(By.ID,"remove-sauce-labs-backpack").click()
# 7) Retourner sur la page d'accueil avec le boutton continue shopping
driver.find_element(By.ID,"continue-shopping").click()
# 8) Remettre 2 articles dans le panier
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
# 9) Retourner dans le panier
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
# 10) Aller au checkout
driver.find_element(By.ID,"checkout").click()
# 11) Remplir les champs demandés
driver.find_element(By.ID,"first-name").send_keys("Alex")
driver.find_element(By.ID,"last-name").send_keys("text")
driver.find_element(By.ID,"postal-code").send_keys("Alextest@gmail.com")
# 12) Cliquer sur continue
driver.find_element(By.ID,"continue").click()
# 13) Cliquer sur finish
driver.find_element(By.ID,"finish").click()
# 14) Cliquer sur Back Home pour revenir à l'écran d'accueil
driver.find_element(By.ID,"back-to-products").click()

time.sleep(4)
# 6) Fermer le navigateur
driver.close()