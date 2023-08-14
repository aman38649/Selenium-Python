from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.get('https://www.freshworks.com/')

wait = WebDriverWait(driver, 10)
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(footer_links))

for ele in footer_links:
    print(ele.text)

wait.until(ec.frame_to_be_available_and_switch_to_it((By.ID, 'test')))
wait.until(ec.element_located_to_be_selected('checkbox'))
wait.until(ec.url_contains('freshworks'))

