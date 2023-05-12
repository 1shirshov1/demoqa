from components.components import WebElement
from pages.base_page import BasePage
class FromPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automaion-practice-from'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstNane')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close.modal = WebElement(driver, '#closeLargeModal')

