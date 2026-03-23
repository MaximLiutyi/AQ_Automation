import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.instagram.com/")
time.sleep(3)

#Валідація url
url = driver.current_url
assert url == "https://www.instagram.com/", "Error in URL"
print("Your URL is:", url)


# Переходимо на сторінку логування
login_form = driver.find_element(By.XPATH,"//input[@name='email']")
login_form.click()
time.sleep(3)

#вводимо та валідуємо мейл
email_input = driver.find_element(By.XPATH,"//input[@name='email']")
email_input.send_keys("Tes@ukr.net") # надсилаємо дані - емайл
time.sleep(2)
print("data email is: ", email_input.get_attribute("value")) # Виводить нам дані які ми ввели в поле мейлу, щоб переконатись що саме потрібні дані пішли

# вводим та валідуєм пароль
password_input = driver.find_element(By.XPATH,"//input[@name='pass']")
password_input.click()
password_input.send_keys("testtesttest")
time.sleep(2)
print("data pass is: ", password_input.get_attribute("value"))

#нажимаєм кнопку увійти
#login_button = driver.find_element(By.XPATH,"//span[text()='Увійти']") # просто по тексту
login_button = driver.find_element(By.XPATH,"(//span[contains(@class, 'x1lliihq ')])[4]") # знайшов кнопку по класу і порядковому номеру
login_button.click()
time.sleep(3)