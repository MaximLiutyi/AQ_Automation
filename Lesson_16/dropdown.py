from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select # for dropdowns

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_location = ("xpath", '//select[@id="dropdown"]')
dropdown = Select(driver.find_element(*dropdown_location))

#--------------вибір по індексу/тексту/value--------------------
#dropdown.select_by_value("2")
#time.sleep(2)
#----------------------------------------------------------

#--------------перебір всіх опцій в дропдауні--------------
all_options = dropdown.options
#print(all_options)

#for option in all_options:
#    time.sleep(1)
#    dropdown.select_by_visible_text(option.text)

#----------------перебір по індесу----------------
#for option in all_options:
#    time.sleep(1)
#    dropdown.select_by_index(all_options.index(option))
#--------------------------------

#---------------- by value-----------------
for option in all_options:
    time.sleep(1)
    dropdown.select_by_value(option.get_attribute("value"))

