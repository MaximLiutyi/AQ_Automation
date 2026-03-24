from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager' # чекає на загрузку коду і стартує
# chrome_options.add_argument("--headless") # запуск у фоновому режимі
# chrome_options.add_argument("incognito") # інкогніто
# chrome_options.add_argument("--disable-extensions") # без розширень
# chrome_options.add_argument("--window-size=1920,1080") # розміри вікна
# chrome_options.add_argument("--disable-cache") # відключає кеш запис

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

start_time = time.time()

driver.get("https://www.instagram.com")

end_time = time.time()
read_time = end_time - start_time
print(read_time)



