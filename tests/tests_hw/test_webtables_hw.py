import time
from pages.webtables_page import WebTablesPage


def test_webtables_crud(browser):
    page = WebTablesPage(browser)
    page.visit()

    first_name = "Kiril"
    last_name = "Kirillov"
    email = "kiril@test.com"
    age = "30"
    salary = "1000"
    department = "QA"

    page.add_button.click()
    assert page.modal_dialog.exist()

    page.submit_button.click()
    assert page.modal_dialog.exist()

    page.first_name.send_keys(first_name)
    page.last_name.send_keys(last_name)
    page.email.send_keys(email)
    page.age.send_keys(age)
    page.salary.send_keys(salary)
    page.department.send_keys(department)

    assert page.first_name.get_attribute("value") == first_name
    assert page.last_name.get_attribute("value") == last_name
    assert page.email.get_attribute("value") == email
    assert page.age.get_attribute("value") == age
    assert page.salary.get_attribute("value") == salary
    assert page.department.get_attribute("value") == department

    page.submit_button.click()
    time.sleep(1)

    assert not page.modal_dialog.visible()



