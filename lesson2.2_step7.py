from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))
  
link = str("http://suninjuly.github.io/file_input.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("ifif@jnfdk.re")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "1.txt"
    file_path = os.path.join(current_dir, file_name)
    input4 = browser.find_element(By.CSS_SELECTOR,"#file")
    input4.send_keys(file_path)
    
    
    button = browser.find_element(By.CSS_SELECTOR,".btn.btn-primary") 
    button.click()
    print(browser.switch_to.alert.text.split()[-1])
    

finally:
    time.sleep(30)
    browser.quit()

