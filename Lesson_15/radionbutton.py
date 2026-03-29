from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/radio-button")

radio_button_yes_location = ("xpath", "(//input[@type='radio'])[1]")
radio_button_no_location = ("xpath", "(//input[@type='radio'])[3]")

#--------------провіряєм чи проставлюється і отримуєм їх статуси----------------
print(driver.find_element(*radio_button_yes_location).is_selected())
driver.find_element(*radio_button_yes_location).click()
print(driver.find_element(*radio_button_yes_location).is_selected())
print(driver.find_element(*radio_button_no_location).is_enabled())

time.sleep(2)