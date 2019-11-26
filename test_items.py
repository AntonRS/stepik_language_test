import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(3)
    result_text_elt = browser.find_element_by_css_selector(".btn-add-to-basket")
    result_text = result_text_elt.text
    new_link = browser.current_url
    if new_link == 'http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/':
        assert result_text == 'Añadir al carrito', "Check es button label"
    elif new_link == 'http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/':
        assert result_text == 'Ajouter au panier', "Check es button label"