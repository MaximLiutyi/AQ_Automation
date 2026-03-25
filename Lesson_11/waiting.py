# явні і неявні очікування

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # очікуванні умови


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


wait = WebDriverWait(driver, 10)
driver.get("https://demoqa.com/dynamic-properties")

# -----------------------------------
# Неявні очікування для всіх елементів
#driver.implicitly_wait(10) # неявне очікування
#button_locate = ('xpath', '//button[@id="visibleAfter"]') # просто як кортеж
#driver.find_element(*button_locate).click() # а тут розпаковка за допомогою *
# --------------------------------------


# ---------------------------------------
# явні очікування для якогось конкретного елемента і прописвувати для кожного окремо
visible_after_button = ('xpath', '//button[@id="visibleAfter"]')

button = wait.until(EC.visibility_of_element_located(visible_after_button)) # Чекаєм наявність елемента на сайті
button.click()
#-------------------------------------------

#-------------------------------------------

clicable_after_button = ('xpath', '//button[@id="enableAfter"]')
button = wait.until(EC.element_to_be_clickable(clicable_after_button)) # Чекаєм поки елемент стане клікабельним
button.click()

#-------------------------------------------