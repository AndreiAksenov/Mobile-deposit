from model.selectors import SELECTORS


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        wd.find_element_by_name('username').click()
        wd.find_element_by_name('username').clear()
        wd.find_element_by_name('username').send_keys(login)
        wd.find_element_by_name('password').click()
        wd.find_element_by_name('password').clear()
        wd.find_element_by_name('password').send_keys(password)
        wd.find_element_by_xpath(SELECTORS['PROCEED']).click()
