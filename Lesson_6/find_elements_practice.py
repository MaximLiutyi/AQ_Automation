import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/")

url = driver.current_url
assert url == "https://hyperskill.org/", "Error in URL"
print("Your URL is: ", url)

time.sleep(5)

#print("Web Elements: ", driver.find_elements("class name", "nav-link"))
list_of_elements = driver.find_elements("class name", "nav-link")
length_of_elements = len(list_of_elements)
print(length_of_elements)
print(list_of_elements)

driver.find_elements("class name", "nav-link")[1].click() # click on element by his index
time.sleep(5)
