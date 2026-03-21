import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.instagram.com/")

url = driver.current_url
assert url == "https://www.instagram.com/", "Error in URL"
print("Your URL is: ", url)

driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[4]/div/a/div').click() # Locating the element and click on it
time.sleep(5)