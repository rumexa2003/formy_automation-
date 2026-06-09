from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import  Select


driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/form"
driver.get(url)
time.sleep(2)
assert"form"in driver.current_url, "failed! login unsuccessful"#to see if user landed in form page 

first_name=driver.find_element(By.ID,"first-name")
first_name.send_keys("Rumexa")

last_name=driver.find_element(By.ID,"last-name")
last_name.send_keys("Dangol")

job=driver.find_element(By.ID,"job-title")
job.send_keys("QA")

ed=driver.find_element(By.XPATH,"//*[@id='radio-button-3']")
ed.click()
time.sleep(2)

s=driver.find_element(By.XPATH,"//*[@id='checkbox-2']")
s.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#to scroll the page to the buttom
time.sleep(2)


dropdown=Select(driver.find_element(By.XPATH,"//*[@id='select-menu']"))
dropdown.select_by_value("1")

date=driver.find_element(By.XPATH,"//*[@id='datepicker']")
date.send_keys("11/11/2020")
time.sleep(2)

submit=driver.find_element(By.XPATH,"/html/body/div/form/div/div[8]/a")
submit.click()
time.sleep(2)

assert"thanks"in driver.current_url, "submission failed! submission unsuccessful"#to see if user landed on the thanks page 


driver.quit()



