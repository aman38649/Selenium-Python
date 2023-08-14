from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.google.com")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')

print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break

time.sleep(5)
driver.quit()

