from pages.elements_page import ElementsPages

def test_find_elements(browser):
    elements_page = ElementsPages(browser)
    elements_pages.visit()
    assert elements_page.btns_fist_menu.check_count_elements(count=9)
