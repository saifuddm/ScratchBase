# Bot For searching product
from selenium import webdriver
# Keys class provides all keys on the keyboard 
from selenium.webdriver.common.keys import Keys
# Used for website waits, to load a delayed element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Emulate mouse movements
from selenium.webdriver.common.action_chains import ActionChains

# Instance of chrome is created 
driver = webdriver.Chrome()
driver.get("https://store.nike.com/ca/en_gb/")
elem = driver.find_element_by_id("TypeaheadSearchInput")
elem.clear()
elem.send_keys("Jordan 1")
elem.send_keys(Keys.RETURN)
# Waits 10s for the screen to show which contry so that can be selected
# Code used for if Nike asked to select which country and language
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"exp-geodetect-notifier__flag"))
    )
finally:
    element.click()
# Having issue here with selector not clicking English properly in the "popup"
driver.implicitly_wait(2)
# "//div[13]//div[2]//div[1]//div[1]//div[4]//div[2]//div[2]//div[1]//a"
englishButton = driver.find_element_by_css_selector("a[href*='/ca/en_gb/']").click()

driver.quit()