from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, "#userName")
        self.current_address = WebElement(driver, "#currentAddress")
        self.submit = WebElement(driver, "#submit")

        self.output_name = WebElement(driver, "#name")
        self.output_current_address = WebElement(driver, "#output #currentAddress", "css")
        self.submit=WebElement(driver, "#submit")
        
