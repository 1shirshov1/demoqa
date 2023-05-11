from pages.demoqa import DemoQa


def test_check_title_demo(browser):
    demo_qa_pages = DemoQa(browser)

    demo_qa_pages.visit()
    assert browser.title == 'demo_qa_pages.pageData['title']'     # <title>DEMOQA</title> - взял с сайта по поиску title.

    self.pageData = {
        'title': 'DemoQa'
    }