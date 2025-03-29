from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    login_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    login_email_input.fill("user.name@gmail.com")

    login_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    login_username_input.fill("username")

    login_password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    login_password_input.fill("password")

    login_registration_input = page.get_by_test_id("registration-page-registration-button")
    login_registration_input.click()

    dashboard_button = page.get_by_test_id("dashboard-drawer-list-item-title-text")
    expect(dashboard_button).to_be_visible()
