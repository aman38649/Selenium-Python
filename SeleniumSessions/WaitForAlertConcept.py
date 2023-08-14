from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.get('https://www.reddit.com/cgi-bin/login.cgi')

driver.find_element(By.NAME, 'proceed').click()

wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()
driver.close()



