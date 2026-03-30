from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/key_presses")

field_location = ("xpath", "//input[@id='target']")
driver.find_element(*field_location).send_keys("asdsad")
driver.find_element(*field_location).send_keys(Keys.CONTROL + "a")
time.sleep(2)