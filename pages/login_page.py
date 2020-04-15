from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert '/login/' in self.browser.current_url, "'Url does not contain '/login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form does not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form does not present"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT)
        password_input.send_keys(password)

        password_confirmation_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRMATION_INPUT)
        password_confirmation_input.send_keys(password)

        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)
        submit_button.click()
