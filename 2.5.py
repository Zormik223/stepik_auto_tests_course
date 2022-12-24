from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    window_before = browser.window_handles[0]
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    x_element = browser.find_element(By.ID, "answer")
    x_element.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()