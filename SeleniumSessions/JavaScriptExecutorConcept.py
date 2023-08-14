from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.get('https://www.amazon.in')

best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
driver.execute_script("arguments[0].click();", best_sellers)

title = driver.execute_script("return document.title;")
print(title)

driver.execute_script("history.go(0);")

# driver.execute_script("alert('hello selenium');")

inner_text = driver.execute_script("return document.documentElement.innerText;")
print(inner_text)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

driver.execute_script("document.getElementById('username').value='aman@gmail.com';")