from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.left_panel_buttons = WebElement(driver, '.element-group:nth-of-type(3) .menu-list li')
        self.icon = WebElement(driver, '#root > header > a > img')

        self.small_modal_button = WebElement(driver, "#showSmallModal", "css")
        self.large_modal_button = WebElement(driver, "#showLargeModal", "css")

        self.close_small_modal_button = WebElement(driver, "#closeSmallModal", "css")
        self.close_large_modal_button = WebElement(driver, "#closeLargeModal", "css")

        self.modal_window = WebElement(driver, ".modal-content", "css")