import time

import pytest
from selenium.webdriver.common.bidi import Browser
from pages.accordion import AccordionsPage
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
from pages.alerts import Alerts


@pytest.mark.parametrize("pages", [AccordionsPage, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.viewport.exist()
    assert page.viewport.grt_dom_attribute('name') == 'viewport'
    assert page.viewport.grt_dom_attribute('content') == 'width=device-width, initial-scale=1'

