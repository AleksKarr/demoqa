from pages.automation_practice_form import AutomationPracticeForm

def test_placeholder_and_empty_submit(browser):
    form_page = AutomationPracticeForm(browser)
    form_page.visit()

    assert form_page.first_name.get_attribute("placeholder") == "First Name"
    assert form_page.last_name.get_attribute("placeholder") == "Last Name"
    assert form_page.user_email.get_attribute("placeholder") == "name@example.com"
    assert form_page.user_email.get_attribute("pattern") == "^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$"

    form_page.submit.click_force()

    assert "was-validated" in form_page.form.get_attribute("class")


def test_login_form_state_and_city(browser):
    form_page = AutomationPracticeForm(browser)
    form_page.visit()

    form_page.state.click_force()
    form_page.state_input.send_keys("NCR")
    form_page.state_input.send_keys("\n")

    form_page.city.click_force()
    form_page.city_input.send_keys("Delhi")
    form_page.city_input.send_keys("\n")

    assert "NCR" in form_page.state.get_attribute("textContent")
    assert "Delhi" in form_page.city.get_attribute("textContent")
