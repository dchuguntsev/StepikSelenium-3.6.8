def test_add_to_card_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")