from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common .action_chains import ActionChains


driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/dragdrop"
driver.get(url)
wait=WebDriverWait(driver,10)
drag=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='image']/img")) )
drop=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='box']")) )
wait= ActionChains (driver)
wait.drag_and_drop(drag,drop).perform()
time.sleep(3)


# address=driver.find_element(By.ID,"autocomplete")
# address.send_keys("123 Maple Street")
time.sleep(5)