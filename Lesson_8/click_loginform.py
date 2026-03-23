import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://english-online.org.ua/channel/James%20engVid")
time.sleep(3)

# Переходимо на сторінку логування
login_button = driver.find_element(By.XPATH,"//a[text()='Увійти']")
login_button.click()
time.sleep(3)

email_input = driver.find_element(By.XPATH,"//input[@type='email']")
email_input.send_keys("Tes@ukr.net") # надсилаємо дані - емайл
time.sleep(3)
print(email_input.get_attribute("value")) # Виводить нам дані які ми ввели в поле мейлу, щоб переконатись що саме потрібні дані пішли

