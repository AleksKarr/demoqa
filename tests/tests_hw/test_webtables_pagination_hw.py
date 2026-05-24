from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.webtables_page import WebTablesPage


def test_webtables_pagination(browser):
    page = WebTablesPage(browser)
    page.visit()

    rows_select = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.-pageSizeOptions select")
        )
    )
    Select(rows_select).select_by_visible_text("5 rows")

    assert page.next_button.get_attribute("disabled") is not None
    assert page.previous_button.get_attribute("disabled") is not None

    data = [
        ("User1", "Test1", "user1@test.com", "21", "1001", "QA"),
        ("User2", "Test2", "user2@test.com", "22", "1002", "QA"),
        ("User3", "Test3", "user3@test.com", "23", "1003", "QA"),
    ]

    for first_name, last_name, email, age, salary, department in data:
        page.add_button.click()
        page.first_name.send_keys(first_name)
        page.last_name.send_keys(last_name)
        page.email.send_keys(email)
        page.age.send_keys(age)
        page.salary.send_keys(salary)
        page.department.send_keys(department)
        page.submit_button.click()

    assert "of 2" in page.page_info.get_text()
    assert page.next_button.get_attribute("disabled") is None

    page.next_button.click()
    assert page.page_jump.get_attribute("value") == "2"

    page.previous_button.click()
    assert page.page_jump.get_attribute("value") == "1"