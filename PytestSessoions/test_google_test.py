from selenium import webdriver
import pytest


driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")


def teardown_module(module):
    driver.quit()


def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"