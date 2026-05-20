import time
from pages.accordion import AccordionsPage


def test_visible_accordion(browser):
    accordions_page = AccordionsPage(browser)
    accordions_page.visit()

    assert accordions_page.section1_content.visible()

    accordions_page.section1_heading.click()
    time.sleep(2)

    assert not accordions_page.section1_content.visible()


def test_visible_accordion_default(browser):
    accordions_page = AccordionsPage(browser)
    accordions_page.visit()

    assert not accordions_page.section2_content_p1.visible()
    assert not accordions_page.section2_content_p2.visible()
    assert not accordions_page.section3_content.visible()