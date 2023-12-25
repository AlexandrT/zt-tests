from .locators import *
from ..elements import BaseElement, TextElement
from ..page import BasePage


class Login(BaseElement):
    locator = SignInPageLocators.LOGIN_INPUT


class Phone(BaseElement):
    locator = SignInPageLocators.PHONE_INPUT


class Password(BaseElement):
    locator = SignInPageLocators.PASSWORD_INPUT


class PhoneCode(BaseElement):
    locator = SignInPageLocators.PHONE_CODE_INPUT


class ErrorMessage(TextElement):
    locator = SignInPageLocators.ERROR_MESSAGE


class SignInForm(BasePage):
    login = Login()
    phone = Phone()
    password = Password()
    phone_code = PhoneCode()
    error_message = ErrorMessage()

    def __init__(self, driver, parent_el):
        self.parent = parent_el
        super().__init__(driver)

    def click_signin_btn(self):
        element = self.find_element_delay(*SignInPageLocators.SIGNIN_BUTTON)
        element.click()

    def click_signup_btn(self):
        element = self.find_element_delay(*SignInPageLocators.SIGNUP_BUTTON)
        element.click()

    def click_phone_tab(self):
        element = self.find_element_delay(*SignInPageLocators.PHONE_TAB)
        element.click()

    def click_continue_btn(self):
        element = self.find_element_delay(*SignInPageLocators.CONTINUE_BUTTON)
        element.click()

    def click_send_btn(self):
        element = self.find_element_delay(*SignInPageLocators.SEND_BUTTON)
        element.click()

    def get_signup_menu_item(self, item_txt):
        return self.find_element_delay(SignInPageLocators.MENU_ITEM(item_txt))


class SignInPage(BasePage):
    def get_signin_form(self):
        return self.find_element_delay(*SignInPageLocators.SIGNIN_FORM)