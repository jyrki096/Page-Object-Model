from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "Login url is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form has not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form has not found"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_first = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_first.send_keys(password)
        password_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FIELD)
        password_repeat.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button_submit.click()

