from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
time.sleep(5)
url="https://www.saucedemo.com/"
driver.get(url)
time.sleep(4)

username=driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")
time.sleep(2)

password=driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
time.sleep(2)

login_button=driver.find_element(By.ID,"login-button")
login_button.click()
time.sleep(2)

assert"inventory"in driver.current_url, "failed! login unsuccessful"#to see if user landed in login page after login in

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#to scroll the inventory page to the buttom
time.sleep(2)

# adding the product to the cart
a=driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
a.click()
time.sleep(2)

b=driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")
b.click()
time.sleep(2)

# scroll the page to the top
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)


cart_button=driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a/span")
cart_button.click()
time.sleep(2)
assert"cart"in driver.current_url, "failed! login unsuccessful"#to see if user landed in cart page 



# checking_out
checkout_button=driver.find_element(By.XPATH,"//*[@id='checkout']")
checkout_button.click()
time.sleep(2)



# filling your information
first_name=driver.find_element(By.XPATH,"//*[@id='first-name']")
first_name.send_keys("Ram")
# time.sleep(2)

last_name=driver.find_element(By.XPATH,"//*[@id='last-name']")
last_name.send_keys("Dhakal")
# time.sleep(2)

portal=driver.find_element(By.XPATH,"//*[@id='postal-code']")
portal.send_keys(15632)
time.sleep(2)

continue_button=driver.find_element(By.XPATH,"//*[@id='continue']")
continue_button.click()
time.sleep(2)


# checkoutstep
finish_button=driver.find_element(By.XPATH,"//*[@id='finish']")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#to scroll the inventory page to the buttom
time.sleep(2)
finish_button.click()


assert"checkout-complete"in driver.current_url, "cannot proceed checkout"#to see if user land  on checkout page
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#to scroll the page buttom
back_home_button=driver.find_element(By.XPATH,"//*[@id='back-to-products']")
back_home_button.click()
time.sleep(2)

assert"inventory"in driver.current_url, "cannot land on inventory page"#to see if user landed in login page after login in
menu_bar=driver.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']")
menu_bar.click()
time.sleep(2)

logout=driver.find_element(By.XPATH,"//*[@id='logout_sidebar_link']")
time.sleep(2)
logout.click()
time.sleep(2)

# assert"saucedemo"in driver.current_url, "failed! login unsuccessful"#to see if user landed in checkout-complete  page 

driver.quit()
