import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)

LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='leftClick']")
RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClick']")
DOUBLE_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClick']")


driver.get("https://testkru.com/Elements/Buttons")

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)

# ланцюг дій з переносом для кращого читання коду через слеш \
actions.click(left_button).pause(1)\
    .double_click(double_button).pause(1)\
    .context_click(right_button).pause(2).perform()

time.sleep(2)