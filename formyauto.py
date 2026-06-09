from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/autocomplete"
driver.get(url)
time.sleep(3)

# address=driver.find_element(By.ID,"autocomplete")
# address.send_keys("123 Maple Street")
time.sleep(5)

street_address=driver.find_element(By.ID,"street_number")
street_address.send_keys("123 Maple Street")
time.sleep(2)

street_address2=driver.find_element(By.ID,"route")
street_address2.send_keys("Apartment 4B")
time.sleep(2)

city=driver.find_element(By.ID,"locality")
city.send_keys("Kathmandu")
time.sleep(2)

state=driver.find_element(By.ID,"administrative_area_level_1")
state.send_keys("Bagmati")
time.sleep(2)

zip=driver.find_element(By.ID,"postal_code")
zip.send_keys("44600")
time.sleep(2)

country=driver.find_element(By.ID,"country")
country.send_keys("Nepal")
time.sleep(2)

driver.quit()