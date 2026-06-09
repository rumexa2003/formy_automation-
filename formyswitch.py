from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
time.sleep(2)

newtab=driver.find_element(By.XPATH,"//*[@id='new-tab-button']")
newtab.click()
time.sleep(2)

print(driver.window_handles)
print(driver.current_window_handle)

driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
print(driver.current_window_handle)

driver.quit()