from .locators import *
from ..page import BasePage


class IdPage(BasePage):
    def get_avatar(self):
        return self.find_element_delay(*IdPageLocators.AVATAR_BLOCK)