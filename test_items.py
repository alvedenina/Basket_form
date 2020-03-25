import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_form(browser):
    browser.get(link)
    # time.sleep(30)
    basket = browser.find_element_by_css_selector(".add-to-basket")
    x = basket.get_attribute("id")
    assert x == "add_to_basket_form", "Кнопка не найдена"




