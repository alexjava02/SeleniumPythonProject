import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 1) Se diriger vers le bon URL
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Frames.html")

# 2) Entrer dans le premier frame
driver.switch_to.frame("SingleFrame")
time.sleep(3)

# 3) Écrire dans le premier frame
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("J'écris dans le premier frame")
time.sleep(1)

# 4) Aller dans le deuxième frame
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()

# 5) Écrire dans le deuxième frame
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']"))
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']"))
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("J'écris dans le deuxième frame")
time.sleep(2)

# 6) Retourner dans le premier frame (dans le but de supprimer ce qui était écrit)
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//a[@href='#Single']").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']"))
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").clear()


time.sleep(3)
driver.quit()