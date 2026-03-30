from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


PROXY_SERVER = "IP" # проставляєм потрібне айпі

options = Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://2ip.ua/ua/")
time.sleep(5)

