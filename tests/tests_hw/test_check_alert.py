from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.alerts_page import AlertsPage


def test_check_alert(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.visit()

    assert alerts_page.timer_alert_button.exist()

    alerts_page.timer_alert_button.click()

    alert = WebDriverWait(browser, 7).until(EC.alert_is_present())

    assert alert is not None
    alert.accept()