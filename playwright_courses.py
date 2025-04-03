import time

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера
    context = browser.new_context()

    page = context.new_page()

    # Открыть страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнить форму регистрации и нажать на кнопку "Registration"
    registration_email_button = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_button.fill("user.name@gmail.com")

    registration_username_button = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_button.fill("username")

    registration_password_button = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_button.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохранить состояние браузера
    context.storage_state(path="browser-state.json")

    # Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
    page = context.new_page()
    #
    # Открыть страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверить наличие и текст заголовка "Courses"
    courses_text = page.get_by_test_id("courses-drawer-list-item-title-text")
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text("Courses")

    # Проверить наличие и текст блока "There is no results"
    empty_result_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(empty_result_text).to_be_visible()
    expect(empty_result_text).to_have_text("There is no results")
