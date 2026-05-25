from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa
import pytest
from pages.radio import RadioButton

# def test_demoqa_h5_headers(browser):
#     page = DemoQa(browser)
#     page.visit()
#
#     headers = browser.find_elements(By.TAG_NAME, "h5")
#
#     assert len(headers) == 6
#
#     for header in headers:
#         assert header.text != ""

@pytest.mark.skip
def test_decor_3(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text !=''

@pytest.mark.skip(True, reasson= 'Просто пропуск')
def test_decor_1(browser):
    radio = RadioButton(browser)

    radio.visit()
    radio.yes.click_force()
    assert radio.text.get_text() == 'You have selected Yes'

    radio.impressive.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'

    assert 'disable' in radio.no.get_dom_attribute('class')

