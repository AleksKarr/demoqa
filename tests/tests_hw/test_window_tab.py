from pages.links_page import LinksPage


def test_window_tab(browser):
    links_page = LinksPage(browser)
    links_page.visit()

    assert links_page.home_link.exist()
    assert links_page.home_link.get_text() == "Home"
    assert links_page.home_link.get_attribute("href") == "https://demoqa.com/"

    old_windows = browser.window_handles
    links_page.home_link.click()

    new_windows = browser.window_handles

    assert len(new_windows) == len(old_windows) + 1