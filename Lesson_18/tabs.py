from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager' # чекає на загрузку коду і стартує
chrome_options.add_argument("--window-size=2560,1440") # розміри вікна

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


wait = WebDriverWait(driver, 10)
driver.get("https://www.youtube.com/")

music_location = ("xpath", "//yt-formatted-string[text()='YouTube Music']")
wait.until(EC.element_to_be_clickable(music_location)).click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0]) # перемикаємось на початкову вкладку
time.sleep(2)
