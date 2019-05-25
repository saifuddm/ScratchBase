# Bot form just the product to end
from selenium import webdriver
# Keys class provides all keys on the keyboard 
from selenium.webdriver.common.keys import Keys
# Used for website waits, to load a delayed element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Emulate mouse movements
from selenium.webdriver.common.action_chains import ActionChains
# For selecting options
from selenium.webdriver.support.ui import Select
import time


# Instance of chrome is created 
driver = webdriver.Chrome()
driver.get("https://store.nike.com/ca/en_gb/pd/clot-air-max-haven-shoe/pid-12566155/pgid-12606118")
sizeDrop = driver.find_element_by_xpath("//span[@class='js-selectBox-label']")
sizeDrop.click()
sizeSelect = driver.find_element_by_xpath("//li[@rel='22957158:M 11 / W 12.5']")
sizeSelect.click()
addToCart = driver.find_element_by_xpath("//button[@id='buyingtools-add-to-cart-button']")
addToCart.click()
driver.implicitly_wait(1)
clickCart = driver.find_element_by_xpath("//i[@class='g72-cart cart-icon']")
clickCart.click()
driver.implicitly_wait(1)
guestCheckout = driver.find_element_by_xpath("//button[@class='js-guestCheckout orange lock']")
guestCheckout.click()

driver.implicitly_wait(5)

# Form Fill
firstName = driver.find_element_by_id("Shipping_FirstName")
firstName.clear()
firstName.send_keys("Murtaza")

lastname = driver.find_element_by_id("Shipping_LastName")
lastname.clear()
lastname.send_keys("Saifuddin")

postCode = driver.find_element_by_id("Shipping_PostCode")
postCode.clear()
postCode.send_keys("l1v1v1")
driver.implicitly_wait(5)

address1 = driver.find_element_by_id("Shipping_Address1")
address1.clear()
address1.send_keys("yupyup")


address3 = driver.find_element_by_id("Shipping_Address3")
address3.clear()
address3.send_keys("Mississauga")


number = driver.find_element_by_id("Shipping_phonenumber")
number.clear()
number.send_keys("1231231234")

email = driver.find_element_by_id("shipping_Email")
email.clear()
email.send_keys("Murtaza@gmail.com")
driver.implicitly_wait(2)
# Failure over here with clicking the button
driver.find_element_by_xpath("//span[@class='checkbox-checkmark']").click()
driver.implicitly_wait(0.3)
driver.find_element_by_id("shippingSubmit").click()
driver.implicitly_wait(0.3)
driver.find_element_by_id("shippingSubmit").click()
driver.implicitly_wait(2)
driver.quit()