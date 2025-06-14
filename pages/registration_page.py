from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы элементов страницы
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.registration_email_button = page.get_by_test_id('registration-form-email-input').locator('input')
        self.registration_username_button = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_password_button = page.get_by_test_id('registration-form-password-input').locator('input')

    def check_disabled_registration_button(self):
        expect(self.registration_button).to_be_disabled()

    def fill_field_email(self, email: str="user.name@gmail.com"):
        self.registration_email_button.fill(email)

    def fill_field_username(self, username: str="username"):
        self.registration_username_button.fill(username)

    def fill_field_password(self, password: str ="password"):
        self.registration_password_button.fill(password)

    def check_enabled_registration_button(self):
        expect(self.registration_button).to_be_enabled()

    def click_registration_button(self):
        self.registration_button.click()
