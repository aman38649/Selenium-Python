from selenium import webdriver
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"],scope='class')
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Documents\\drivers\\chromedriver.exe")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_Google(BaseTest):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"


    def test_google_url(self):
        self.driver.get("http://www.google.com")
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"