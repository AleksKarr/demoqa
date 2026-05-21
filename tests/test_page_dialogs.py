from pages.modal_dialogs import ModalDialogsPage
import time


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogsPage(browser)

    modal_dialogs_page.visit()

    assert modal_dialogs_page.left_panel_buttons.check_count_elements(5)


def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogsPage(browser)

    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()

    modal_dialogs_page.icon.click_force()
    modal_dialogs_page.back()

    browser.set_window_size(900, 400)
    time.sleep(2)
    modal_dialogs_page.forward()

    assert browser.current_url.rstrip("/") == "https://demoqa.com".rstrip("/")
    assert browser.title == "demosite"

    browser.set_window_size(1000, 1000)