import utils
import logging
import config
from utils.data import TestData as td
from pages.login_page import LoginPage
from tests.test_base import BaseTest
import pytest_check as check
import pytest
import time
import utils.custom_logger as cl

log = cl.customLogger(logging.INFO)


class TestLogin(BaseTest):

    """ We can use following method to pass LoginPage objects """
    @pytest.fixture
    def login_page_object(self):
        self.page = LoginPage(self.driver)

    def test_validate_page_title(self, login_page_object):
        title = self.page.get_page_title()
        check.equal(title, td.MAIN_PAGE_TITLE)

    def test_validate_user_login_link_existence(self, login_page_object):
        user_login_link_exists = self.page.is_login_link_exists()
        check.is_true(user_login_link_exists, "Assert if Users Login link exist on Main page")

    def test_navigate_to_login_page(self, login_page_object):
        self.page.click_on_login_page()
        title = self.page.get_page_title()
        check.equal(title, td.LOGIN_PAGE_TITLE, "Assert if Title matches on LogIn page")
        config.url = self.driver.current_url

    def test_validate_sign_up_link_exists(self, login_page_object):
        self.driver.get(config.url)
        time.sleep(5)
        sign_up_link = self.page.is_sign_up_link_exists()
        check.is_true(sign_up_link, "Assert if Sign Up link exists on User LogIn page")

    def test_validate_username_field(self, login_page_object):
        self.driver.get(config.url)
        username = self.page.is_username_field_exists()
        check.is_true(username, "Assert if Username field exists on User Login page")

    def test_validate_password_field(self, login_page_object):
        self.driver.get(config.url)
        password = self.page.is_password_field_exists()
        check.is_true(password, "Assert if Password field exists on User Login page")

    def test_validate_login_button_exists(self, login_page_object):
        self.driver.get(config.url)
        login_button = self.page.is_login_button_exists()
        check.is_true(login_button, "Assert if Password field exists on User Login page")

    def test_login(self, login_page_object):
        self.driver.get(config.url)
        self.page.login(td.USER_NAME, td.USER_PASSWORD)
        title = self.page.get_page_title()
        check.equal(title, td.MAIN_PAGE_TITLE, "Assert if Title matches on LogIn page")