from pages.base_page import BasePage
from components.components import WebElement


class AutomationPracticeForm(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, "#firstName", "css")
        self.last_name = WebElement(driver, "#lastName", "css")
        self.user_email = WebElement(driver, "#userEmail", "css")

        self.submit = WebElement(driver, "#submit", "css")
        self.form = WebElement(driver, "form", "css")

        self.state = WebElement(driver, "#state", "css")
        self.city = WebElement(driver, "#city", "css")
        self.state_input = WebElement(driver, "#react-select-3-input", "css")
        self.city_input = WebElement(driver, "#react-select-4-input", "css")