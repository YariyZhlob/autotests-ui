from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Открыть страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка Registration не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    #Заполнить поле Email значением
    registration_email_button = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_button.fill("user.name@gmail.com")

    # Заполнить поле Username
    registration_username_button = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_button.fill("username")

    # Заполнить поле Password
    registration_password_button = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_button.fill("password")

    # Проверить, что кнопка "Registration" перешла в состояние enabled
    expect(registration_button).to_be_enabled()
