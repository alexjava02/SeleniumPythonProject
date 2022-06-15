import time

from selenium import webdriver

driver = webdriver.Chrome()

# Ouvrir la fenêtre en plein écran
driver.maximize_window()

# Obtenir l'url de la page
driver.get("https://demo.nopcommerce.com/")
url_page = driver.current_url
print(url_page)

# Obtenir title
titre_page = driver.title
print(titre_page)

# Obtenir code source
source_page = driver.page_source
print((source_page))

# Fin du programme
time.sleep(3)
driver.quit()