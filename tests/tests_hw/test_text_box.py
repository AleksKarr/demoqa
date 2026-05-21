from pages.text_box import TextBox


def test_text_box_submit(browser):
    text_box_page = TextBox(browser)

    full_name_text = "Kiril Kirillov"
    current_address_text = "Piter, Piter"

    text_box_page.visit()

    text_box_page.full_name.send_keys(full_name_text)
    text_box_page.current_address.send_keys(current_address_text)

    text_box_page.submit.click_force()

    assert text_box_page.output_name.get_text() == f"Name:{full_name_text}"
    assert text_box_page.output_current_address.get_text() == f"Current Address :{current_address_text}"