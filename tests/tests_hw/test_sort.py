from pages.webtables_page import WebTablesPage


def test_sort(browser):
    page = WebTablesPage(browser)
    page.visit()

    headers = [
        page.first_name_header,
        page.last_name_header,
        page.age_header,
        page.email_header,
        page.salary_header,
        page.department_header,
    ]

    for header in headers:
        header.click()
        assert "sort-asc" in header.get_attribute("class") or "sort-desc" in header.get_attribute("class")