from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    y_element = browser.find_element(By.ID, "num1")
    z_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = z_element.text
    x = str(int(y)+int(z))

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()