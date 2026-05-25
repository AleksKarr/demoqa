from pages.base_page import BasePage
from components.components import WebElement

class RadioButton(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.radio_button = WebElement(driver, "#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7 > h1", "css")

