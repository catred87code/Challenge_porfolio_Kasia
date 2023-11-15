from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    language_field_xpath = "//input[contains(@class, 'nativeInput)]"
    login_label_xpath = "//*[@id='login-label']"
    password_label_xpath = "//*[@id='password-label']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
