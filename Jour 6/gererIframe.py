import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# Entrer dans le frame
driver.switch_to.frame("packageListFrame")
time.sleep(3)

# Cliquez sur le lien
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(2)

# Sortir du premier frame pour retourner à la page par défaut
driver.switch_to.default_content()

# Changer de frame pour pouvoir aller cliquer sur WebDriver
driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH, "/html/body/main/div/section[1]/ul/li[14]/a/span").click()

# Cliquez sur Help
driver.switch_to.default_content()
#driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()


time.sleep(3)
driver.quit()



