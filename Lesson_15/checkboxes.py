from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#----------спосіб 1 отримання статусу чекбокса---------------
driver.get("https://the-internet.herokuapp.com/checkboxes")
locator_checkbox1 = ("xpath", "(//input[@type='checkbox'])[1]")
#print(driver.find_element(*locator_checkbox1).get_attribute("checked"))
#driver.find_element(*locator_checkbox1).click()
#print(driver.find_element(*locator_checkbox1).get_attribute("checked"))
#time.sleep(2)


#---------спосіб 2отримання статусу чекбокса-------------------
print(driver.find_element(*locator_checkbox1).is_selected())
driver.find_element(*locator_checkbox1).click()
print(driver.find_element(*locator_checkbox1).is_selected())