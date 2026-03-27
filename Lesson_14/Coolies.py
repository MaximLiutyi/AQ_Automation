##########working with cookies##############
# Додаєм товар у кошик
# Берем кукі
# Видалаєм кукі в браузері
# рефреш  браузер
# загружаєм кукі
############################################


import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import pickle
from selenium.webdriver.support import expected_conditions as EC # очікуванні умови
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get("https://prom.ua/ua/p2450781834-istochnik-besperebojnogo-pitaniya.html")
buy_botton_location = ("xpath", '//button[contains(@class, "I80Um DuFM2 vFL5E R64la zw0Z3")]')
wait.until(EC.element_to_be_clickable(buy_botton_location)).click()
time.sleep(5)

# Берем кукі кошика
pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb")) # saving cookies in the directory

# видаляєм кукі з браузера
driver.delete_all_cookies()

#рефреш сторінки, з кошика має пропасти
driver.refresh()
time.sleep(5)

# загружаєм кукі
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(10)

#---------------------------#adding cookies-------------------

#driver.add_cookie({
#    "name": "Test",
#    "value": "Test2"
#})
#time.sleep(2)

#-------------------------------------------------------------

