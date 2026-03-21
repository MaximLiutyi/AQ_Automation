import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0")

# Validation of the URL
url = driver.current_url
assert url == "https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0", "Error in URL, wrong url"

# Validation of the Tittle
current_tittle = driver.title
assert current_tittle == "Вікіпедія", "Error in Title"

print("URL of the page: ", url)
print("Title of the page: ", current_tittle)

time.sleep(3)

# if we need to receive the whole code of the page
#print(driver.page_source)