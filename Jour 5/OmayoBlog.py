import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Script qui permet de sélectionner et déselectionner des options dans le dropdown dans une Multi Selection Box

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

# 1) Sélectionner le drop "Older Newsletter"
drop = driver.find_element(By.ID, "drop1")
doc = Select(drop)

# 2) Sélectionner le dropdown par texte
doc.select_by_visible_text("doc 1")

# 3) Sélectionner les options dans le Selection box
multiselect = driver.find_element(By.ID, "multiselect1")
selectionner = Select(multiselect)
selectionner.select_by_value("volvox")
selectionner.select_by_value("audix")
time.sleep(3)

# 4) Désélectionner les options et en choisir une nouvelle dans le drop down
selectionner.deselect_by_value("volvox")
selectionner.deselect_by_value("audix")
doc.select_by_visible_text("doc 4")

# 5) sélectionner d'autres options dans le selection box
selectionner.select_by_value("swiftx")
selectionner.select_by_value("Hyundaix")

time.sleep(3)
driver.close()