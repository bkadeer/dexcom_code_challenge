from selenium.webdriver.common.by import By

from utils.data import TestData
from pages.base_page import BasePage


class LoginPage(BasePage):
    """ locators """
    USER_LOGIN_LINK = (By.XPATH, "//*[contains(text(), 'Dexcom Clarity for Home Users')]")
    EMAIL_FIELD = (By.ID, "username")
    PW_FIELD = (By.ID, "password")
    BUTTON_LOGIN = (By.NAME, "op",)
    # SIGNUP_LINK = (By.XPATH, "//button[text()[contains(.,'Sign Up')]]")
    SIGNUP_LINK = (By.XPATH, "//button[text()='Sign Up']")

    """ constructor of the page class """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ page actions """
    def is_login_link_exists(self):
        return self.is_enabled(self.USER_LOGIN_LINK)

    def get_page_title(self):
        return self.get_title()

    def login(self, username, pw):
        self.send_keys(self.EMAIL_FIELD, username)
        self.send_keys(self.PW_FIELD, pw)
        self.click_on_element(self.BUTTON_LOGIN)

    def click_on_login_page(self):
        self.click_on_element(self.USER_LOGIN_LINK)

    def is_sign_up_link_exists(self):
        return self.is_enabled(self.SIGNUP_LINK)

    def is_username_field_exists(self):
        return self.is_enabled(self.EMAIL_FIELD)

    def is_password_field_exists(self):
        return self.is_enabled(self.PW_FIELD)

    def is_login_button_exists(self):
        return self.is_enabled(self.BUTTON_LOGIN)
