import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

# Trouver le boutton Click for JS Alert
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()

# Récupérer l'alerte à l'aide d'une variable dans le cas d'utilisation répété
alertWindow = driver.switch_to.alert
# Afficher l'alerte dans la console
print(alertWindow.text)

# Cliquez sur le boutton OK de l'alerte (dismiss = cancel)
alertWindow.accept()

time.sleep(5)
driver.quit() #Ferme toute les fenêtres ouverte par le script (driver.close() = ferme seulement 1 fenêtre)