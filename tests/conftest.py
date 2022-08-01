import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.data import TestData
from pages.base_page import BasePage


# def pytest_addoptions(parser):
#     parser.addoption("--browser_mode", action="store", default="yes", hepl="Run Tests in headless mode")
#
#
# @pytest.fixture(scope='session')
# def browser(pytestconfig):
#     return pytestconfig.getoption('browser_mode')


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument("user-data-dir=/Users/admin/Library/Application Support/Google/Chrome/Default")
    # options.add_argument('--headless')
    if request.param == "chrome":
        web_driver = webdriver.Chrome(options=options, executable_path=TestData.CHROME_PATH)
    # elif request.param == "firefox":
    #     web_driver = webdriver.Firefox(options=options, executable_path=TestData.FIREFOX_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    # web_driver.quit()

# @pytest.fixture()
# def get_base_url()
