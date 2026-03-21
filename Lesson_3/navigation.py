from time import sleep # імпортуєм час

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com") # відкриваєм URL
time.sleep(20) # чекаєм скільки потрібно

driver.back() # направляє назад
time.sleep(3)

driver.refresh() # оновляє сторінку
time.sleep(3)

driver.forward() # направляє вперед
time.sleep(3)