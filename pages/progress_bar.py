from pages.base_page import BasePage
from components.components import WebElement

class ProgressBar(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)

        self.button = WebElement(driver, "#startStopButton", "css")
        self.bar = WebElement(driver, ".progress-bar", "css")
