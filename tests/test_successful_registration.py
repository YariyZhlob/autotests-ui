from pages.registration_page import RegistrationPage
from pages.dashboardpage import DashboardPage


def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    # Шаг 1: открыть страницу регистрации
    registration_page.visit(url="https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Шаг 2: заполнить форму
    registration_page.fill_field_email()
    registration_page.fill_field_username()
    registration_page.fill_field_password()

    # Шаг 3: убедиться, что кнопка активна, и отправить форму
    registration_page.check_enabled_registration_button()
    registration_page.click_registration_button()

    # Шаг 4: проверка, что пользователь оказался на дашборде
    registration_page.page.wait_for_url("**/dashboard")  #URL меняется
    dashboard_page.check_visible_dashboard_button()
