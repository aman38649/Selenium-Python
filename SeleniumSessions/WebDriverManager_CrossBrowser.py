from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
import time

browserName = "safari"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
else:
    print("Please enter the correct browser name:"+ browserName)
    raise Exception('driver not found')

driver.implicitly_wait(5)

driver.get("https://app.hubspot.com/login")

driver.find_element(By.ID, 'username').send_keys("naveenanimation30@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Test@12345")
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)

time.sleep(4)
driver.quit()

