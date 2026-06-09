from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/scroll"
driver.get(url)
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

full_name=driver.find_element(By.ID,"name")
full_name.send_keys("Ram Dhakal")
time.sleep(2)

date=driver.find_element(By.ID,"date")
date.send_keys("02/14/2020")
time.sleep(2)

driver.quit()