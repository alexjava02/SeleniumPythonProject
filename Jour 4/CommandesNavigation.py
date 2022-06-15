import time

from selenium import webdriver

driver = webdriver.Chrome

driver.get("https://demo.nopcommerce.com/")
time.sleep(2)

driver.get("https://www.google.com")
time.sleep(3)
driver.back() # Appuyer sur la flèche précédent du navigateur
time.sleep(3)

driver.forward() # Appuyer sur la flèche suivant du navigateur
time.sleep(3)

driver.refresh() # Appuyer sur refresh du navigateur
time.sleep(3)


driver.close()