from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

import time
driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

username_url = driver.find_element(By.ID, 'Form_getForm_subdomain_Holder')
full_name = driver.find_element(By.ID, 'Form_getForm_Name_Holder')
email = driver.find_element(By.ID, 'Form_getForm_Email_Holder')
contact = driver.find_element(By.ID, 'Form_getForm_Contact_Holder')
feature_link = driver.find_element(By.LINK_TEXT, 'Get Your Free Trial')

username_url.send_keys("naveenautomationlabs")
full_name.send_keys("Naveen")
email.send_keys("naveen@gmail.com")
contact.send_keys("8989654537")
feature_link.click()

