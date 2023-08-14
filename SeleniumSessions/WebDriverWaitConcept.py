from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.get('https://appp.hubspot.com/login')
wait = WebDriverWait(driver, 3)
# wait.until(ec.title_is('HubSpot Login'))
wait.until(ec.title_contains("HubSpot"))

print(driver.title)

email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_id.send_keys('test@gmail.com')

driver.find_element(By.ID, 'password').send_keys("test@12345")

