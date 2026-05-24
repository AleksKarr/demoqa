from pages.base_page import BasePage
from components.components import WebElement


class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/webtables")

        self.rows_select = WebElement(driver, "select[aria-label='rows per page']", "css")
        self.add_button = WebElement(driver, "#addNewRecordButton", "css")
        self.modal_dialog = WebElement(driver, "#registration-form-modal", "css")
        self.submit_button = WebElement(driver, "#submit", "css")

        self.first_name = WebElement(driver, "#firstName", "css")
        self.last_name = WebElement(driver, "#lastName", "css")
        self.email = WebElement(driver, "#userEmail", "css")
        self.age = WebElement(driver, "#age", "css")
        self.salary = WebElement(driver, "#salary", "css")
        self.department = WebElement(driver, "#department", "css")

        self.next_button = WebElement(driver, "#next-page", "css")
        self.previous_button = WebElement(driver, "#previous-page", "css")
        self.page_info = WebElement(driver, ".-pageInfo", "css")
        self.page_jump = WebElement(driver, "input[aria-label='jump to page']", "css")