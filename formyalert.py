from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
time.sleep(3)

abutton=driver.find_element(By.ID,"alert-button")
abutton.click()
alert=driver.switch_to.alert
alert.dismiss()
time.sleep(2)
driver.quit()