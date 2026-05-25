from pages.slider_page import Slider


def test_slider_v1(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.inp.exist()

    slider.slider.inp_send_keys('50')
    slider.slider.send_keys('50')

    assert slider.inp.get_dom_attribute('value') == '50'


def test_slider_v3(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.slider_inp.exist()

    while not slider.inp.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.inp.get_dom_attribute('value') == '50'