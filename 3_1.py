import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

 
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
    
class TestBlock(unittest.TestCase):
    def test1(self):
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
    def test2(self):
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
    def test3(self):
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("email@gmail.com")
        
if __name__ == "__main__":
    unittest.main()

# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
    
time.sleep(10)
browser.quit()