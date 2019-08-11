from model.selectors import SELECTORS


class LoginPage:

    def __init__(self, app):
        self.app = app

    def close_notification(self):
        wd = self.app.wd
        wd.find_element_by_class_name('close').click()

    def repair_password(self, email):
        wd = self.app.wd
        #ничего кроме link_text не работает, или работает только один раз
        wd.find_element_by_link_text('Forgot password').click()
        wd.find_element_by_name('forgotPass').click()
        wd.find_element_by_name('forgotPass').clear()
        wd.find_element_by_name('forgotPass').send_keys(email)
        wd.find_element_by_xpath(SELECTORS['REPAIR PASSWORD']).click()
