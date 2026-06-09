from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/fileupload"
driver.get(url)
time.sleep(2)
assert"fileupload"in driver.current_url, "failed!"


file=driver.find_element(By.XPATH,"//*[@id='file-upload-field']")
file.send_keys(r"E:\QA\python\dog.jpg")
time.sleep(2)

driver.quit()