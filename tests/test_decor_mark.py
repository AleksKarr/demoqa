import pytest


@pytest.mark.smoke
def test_mark_1(browser):
    assert True


@pytest.mark.regress
def test_mark_2(browser):
    assert True

@pytest.mark.regress
def test_mark_3(browser):
    assert True


@pytest.mark.regress
def test_mark_4(browser):
    assert True