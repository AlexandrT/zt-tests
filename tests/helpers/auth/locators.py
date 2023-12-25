from selenium.webdriver.common.by import By


class SignInPageLocators(object):
    LOGIN_INPUT = (By.ID, 'passp-field-login')
    PHONE_INPUT = (By.ID, 'passp-field-phone')
    PASSWORD_INPUT = (By.ID, 'passp-field-passwd')
    PHONE_CODE_INPUT = (By.ID, 'passp-field-phoneCode')

    SIGNIN_BUTTON = (By.ID, 'passp:sign-in')
    SIGNUP_BUTTON = (By.ID, 'passp:exp-register')
    CONTINUE_BUTTON = (By.ID, 'passp:phone:controls:next')
    SEND_BUTTON = (By.XPATH, '//button[@data-t="button:action"]')

    ERROR_MESSAGE = (By.ID, 'field:input-login:hint')

    SIGNIN_FORM = (By.XPATH, '//form')

    PHONE_TAB = (By.XPATH, '//button[@data-type="phone"]')

    MENU_ITEM = lambda item_txt: (By.XPATH, f'//button[.="{item_txt}"]')


class IdPageLocators(object):
    AVATAR_BLOCK = (By.CLASS_NAME, 'UserID-Avatar')
