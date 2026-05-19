from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/accordian")

        self.section1_content = WebElement(driver, "#section1Content > p")
        self.section1_heading = WebElement(driver, "#section1Heading")
        self.section2_content_p1 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.section2_content_p2 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.section3_content = WebElement(driver, "#section3Content > p")