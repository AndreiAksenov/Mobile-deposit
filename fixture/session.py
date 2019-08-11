

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        wd.find_element_by_name('username').send_keys(login)
        wd.find_element_by_name('password').send_keys(password)
        wd.find_element_by_link_text('PROCEED').click()
