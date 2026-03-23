import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://sinoptik.ua/pohoda/piddnistriany")
time.sleep(3)

url = driver.current_url
assert url == "https://sinoptik.ua/pohoda/piddnistriany", "Error in URL"
print("Your URL is:", url)

driver.find_element(By.XPATH, '//a[contains(@class, "R9FWZvBo")]').click()
time.sleep(3)