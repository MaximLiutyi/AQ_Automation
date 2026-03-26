
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # очікуванні умови
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/alerts")

button_location = ("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(button_location)).click()
time.sleep(2)

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert
print(alert.text)
alert.dismiss() #відхилити алерт


time.sleep(2)