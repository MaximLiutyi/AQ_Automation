import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = webdriver.ChromeOptions()

prefs = {"download.default_directory": f"{os.getcwd()}/Lesson_10/downloads" } # нова дефолтна папка для скачування
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://the-internet.herokuapp.com/download")

driver.find_elements("xpath", '//a')[2].click()
time.sleep(4)


# для загрузки файлів використовуємо і реалізовуємо через input
