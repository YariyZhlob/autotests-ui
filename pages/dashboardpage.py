from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локатор элемента
        self.dashboard_button = page.get_by_test_id("dashboard-drawer-list-item-title-text")

    def check_visible_dashboard_button(self):
        expect(self.dashboard_button).to_be_visible()

