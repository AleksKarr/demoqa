import time

from pages.text_box import TextBox

def test_placeholder(browser):
    tex_tbox_page = TextBox(browser)

    tex_tbox_page.visit()
    assert tex_tbox_page.name.get_dom_attribute('placeholder') == 'Full Name'
