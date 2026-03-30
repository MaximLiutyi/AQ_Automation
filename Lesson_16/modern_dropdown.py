from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

select_one_locator = ("xpath", "//input[@id='react-select-3-input']")
multiselect_locator = ("xpath", "//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu")
time.sleep(2)
driver.find_element(*multiselect_locator).send_keys("Red", Keys.ENTER)
driver.find_element(*multiselect_locator).send_keys("Black", Keys.ENTER)

time.sleep(2)

