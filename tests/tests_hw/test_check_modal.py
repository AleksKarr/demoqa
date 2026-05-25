import pytest
import time
from pages.modal_dialogs import ModalDialogsPage


def test_check_modal(browser):
    modal_page = ModalDialogsPage(browser)
    modal_page.visit()

    if "demoqa.com" not in browser.current_url:
        pytest.skip("Страница недоступна")

    assert modal_page.small_modal_button.exist()
    assert modal_page.large_modal_button.exist()

    modal_page.small_modal_button.click()
    assert modal_page.modal_window.visible()

    modal_page.close_small_modal_button.click()
    time.sleep(1)
    assert not modal_page.modal_window.visible()

    modal_page.large_modal_button.click()
    assert modal_page.modal_window.visible()

    modal_page.close_large_modal_button.click()
    time.sleep(1)
    assert not modal_page.modal_window.visible()