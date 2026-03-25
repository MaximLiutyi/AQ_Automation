from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # очікуванні умови
import time

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled") # робить нас від ролі користувача
options.add_argument("--user-agent=Seleniun") # брати з сайтів різних юзер агентів

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)


driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(3)
#driver.save_screenshot("name.png") # робить скріншоти