from model.selectors import SELECTORS

class PaymentHelper:

    def __init__(self, app):
        self.app = app

    def select_status(self, status):
        wd = self.app.wd
        wd.find_element_by_name(status).click()

    def get_amount(self, current):
        wd = self.app.wd
        amount = wd.find_element_by_css_selector('.you-get > .value').text
        if current == 'RUB':
            clear_amount = str(amount).split(' ')
            return int(clear_amount[0])
        else:
            return int(amount[1:])

    def select_currency(self, currency):
        wd = self.app.wd
        wd.find_element_by_css_selector('.currency .current').click()
        wd.find_element_by_xpath(SELECTORS[currency]).click()

    def open_payment_system_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.payment-system-selector .current.image').click()

    def select_payment_system(self, selector):
        wd = self.app.wd
        wd.find_element_by_xpath(selector).click()

    def selected_payment_system(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector('.current.image .title').text

    def apply(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('submit .submit').click()

    def back_to(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.back .dashed-link').click()

    def input_phone(self):
        wd = self.app.wd
        wd.find_element_by_name('phone').send_keys('9133652145')

