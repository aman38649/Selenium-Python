from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.implicitly_wait(10)

# dynamic wait
# imp wait will be applied for all the web elements
# only of web elements
# not for non web elements : title, url, alerts

driver.get('https://appp.hubspot.com/login')
print(driver.title)
user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("test@gmail.com")
driver.find_element(By.ID, 'password').send_keys("test@12345")

driver.implicitly_wait(0) # nullify of implicit wait





