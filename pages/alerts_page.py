from pages.base_page import BasePage
from components.components import WebElement


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/alerts")

        self.timer_alert_button = WebElement(driver, "#timerAlertButton", "css")