from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # очікуванні умови
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

#--------------------------------
remove_buton_location = ("xpath", "//button[text()='Remove']")
driver.find_element(*remove_buton_location).click()
wait.until(EC.invisibility_of_element_located(remove_buton_location)) #очікуєм допоки елемент пропаде
#----------------------------------

enable_button_location = ("xpath", "//button[text()='Enable']")
text_input_location = ("xpath", "//input[@type='text']")

# клікаєм на кнопку щоб активувати поле для ввода
wait.until(EC.element_to_be_clickable(enable_button_location)).click()
wait.until(EC.element_to_be_clickable(text_input_location)).send_keys("Hello World") # вводим в поле
wait.until(EC.text_to_be_present_in_element_value(text_input_location, "Hello World")) # перевіряєм що воно ввелось
print("All good")
time.sleep(5)