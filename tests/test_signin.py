import pytest

from helpers.auth.signin_page import SignInPage, SignInForm
from lib.config import settings
from tests.helpers.assertions import assert_element_present, assert_field_error
from tests.helpers.auth.id_page import IdPage


class TestAuth():
    @pytest.mark.parametrize(
        "login",
        [
            settings.VALID_CREDENTIALS['email'],
            settings.VALID_CREDENTIALS['login']
        ]
    )
    def test_signin_by_login_or_email_ok(self, selenium, login):
        selenium.get(settings.BASE_URL)

        signin_page = SignInPage(selenium)
        signin_form = SignInForm(selenium, signin_page)

        signin_form.login = login
        signin_form.click_signin_btn()

        signin_form.password = settings.VALID_CREDENTIALS['password']
        signin_form.click_signin_btn()

        id_page = IdPage(selenium)
        avatar = id_page.get_avatar()
        assert_element_present(avatar)

    def test_signin_by_phone_ok(self, selenium, phone, phone_code):
        selenium.get(settings.BASE_URL)

        signin_page = SignInPage(selenium)
        signin_form = SignInForm(selenium, signin_page)

        signin_form.click_phone_tab()

        signin_form.phone = phone
        signin_form.click_continue_btn()

        signin_form.phone_code = phone_code
        signin_form.click_send_btn()

        id_page = IdPage(selenium)
        avatar = id_page.get_avatar()
        assert_element_present(avatar)

    def test_create_id(self, selenium):
        selenium.get(settings.BASE_URL)

        signin_page = SignInPage(selenium)
        signin_form = SignInForm(selenium)

        signin_form.click_create_id_btn()

        [ assert_element_present(signin_form.get_signup_menu_item(item_txt))
          for item_txt in self.translator.get_translator(
                'zt.signup.button_items') ]

    def test_login_not_existed(self, selenium, not_existed_login):
        selenium.get(settings.BASE_URL)

        signin_page = SignInPage(selenium)
        signin_form = SignInForm(selenium)

        signin_form.login = not_existed_login

        signin_form.click_signin_btn()

        assert_field_error(signin_form.login)