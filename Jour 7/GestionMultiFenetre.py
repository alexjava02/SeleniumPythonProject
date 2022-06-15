import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Mettre le ID de la première fenêtre dans une variable
parentWindowID = driver.current_window_handle
print(parentWindowID) # ID trouvé : CDwindow-029123FD567390C73FD0EF7717BF8FBB

# Cliquez sur "OrangeHRM, Inc" au bas de la page
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

# Récupérer la liste des IDs de fenêtre ouverte
windowHandlesIDs = driver.window_handles
# 1ere fenêtre
parentWindowID = windowHandlesIDs[0]
# 2ième fenêtre
childWindowID = windowHandlesIDs[1]

# Les ID trouvés sont dynamiques, change à chaque exécution
print("parentWindowID : " +parentWindowID) # ID trouvé : parentWindowID : CDwindow-99382789348849C06874971B09D08C82
print("childWindowID : " +childWindowID) # ID trouvé : childWindowID : CDwindow-8EAA8A337A17F9BED503C2580A2EFB9D

# Basculer vers la 2ième fenêtre, récupérer son url et son titre
driver.switch_to.window(childWindowID) # Si on ne switch pas il prendra la première fenêtre par défaut
url2 = driver.current_url
title2 = driver.title
print(url2)
print(title2)

# 2ièeme approche
for winID in windowHandlesIDs:
    driver.switch_to.window(winID)
    if driver.title == title2:
        driver.close()

time.sleep(3)
driver.quit()

