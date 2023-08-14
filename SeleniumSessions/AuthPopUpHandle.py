from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')