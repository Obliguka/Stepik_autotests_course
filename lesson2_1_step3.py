from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = str("https://suninjuly.github.io/math.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
    input3 = browser.find_element(By.CSS_SELECTOR,"#answer")
    print(x_element.text)
    x = x_element.text
    y = calc(x)
    input3.send_keys(y)
    input4 = browser.find_element(By.CSS_SELECTOR,"#robotCheckbox")
    input4.click()
    input5 = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
    input5.click()
    input6 = browser.find_element(By.CSS_SELECTOR,"button")
    input6.click()
	
    
    
    
    
	
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла