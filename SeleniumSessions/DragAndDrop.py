from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://jqueryui.com/resources/demos/droppable/default.html')

'''drag and drop'''
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

act_chains = ActionChains(driver)
#act_chains.drag_and_drop(source,target).perform()

act_chains\
    .click_and_hold(source)\
    .move_to_element(target)\
    .release()\
    .perform()