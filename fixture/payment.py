

class PaymentHelper:

    def __init__(self, app):
        self.app = app

    def title(self):
        wd = self.app.wd
        return wd.find_element_by_link_text('STATUS PRIVILEGES DESCRIPTION').text