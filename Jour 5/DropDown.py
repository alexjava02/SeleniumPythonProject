import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")

drop_country = driver.find_element(By.ID, "input-country")
country = Select(drop_country)
# 1) Sélectionner le pays par texte
#country.select_by_visible_text("Canada")

# 2) Sélectionner le pays par l'index (1 est le premier)
#country.select_by_index(26)

# 3) Sélectionner par le numéro associé à value (Canada = 38)
#country.select_by_value(38)

# 4) Afficher le nombre total d'options du dropdown
all_options = country.options
total_options = len(all_options)
print("Le nombre total d'options est : ", total_options)

# 5) Afficher toutes les options de la liste du dropdown (les noms)
#for opt in all_options:
#    print(opt.text)

# Façon de sélectionner Canada avec une boucle
#for opt in all_options:
#    if opt.text == "Canada":
#       opt.click()
#        break



time.sleep(3)

driver.close()
