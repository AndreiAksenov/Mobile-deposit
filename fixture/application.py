from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.localization import LocalizationHelper
from fixture.login_page import LoginPage
from fixture.navigation import NavigationHelper
from fixture.payment import PaymentHelper
from fixture.session import SessionHelper
from model.users import Users


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.payment = PaymentHelper(self)
        self.localization = LocalizationHelper(self)
        self.navigation = NavigationHelper(self)
        self.login_page = LoginPage(self)

    def experiment(self):
        self.wd.find_element_by_xpath()
        self.wd.find_element_by_class_name('forgot')
        self.wd.find_element_by_link_text('Forgot password')
        self.wd.find_element_by_css_selector()

    def check_exists_by_class_name(self, name):
        try:
            self.wd.find_elements_by_class_name(name)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_xpath(self, xpath):
        try:
            self.wd.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def destroy(self):
        self.wd.quit()
