from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("https://www.instagram.com/")

# Валідація URL
url = driver.current_url
assert url == "https://www.instagram.com/", "Error in URL"
print("Your URL is:", url)

# Username
username = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='email']"))
)
username.send_keys("your_username")

# Password
password_input = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='pass']"))
)

password_input.send_keys("your_password")

# Login button
login_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Увійти']"))
)
login_btn.click()
time.sleep(2)