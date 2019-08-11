from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.localization import LocalizationHelper
from fixture.navigation import NavigationHelper
from fixture.payment import PaymentHelper
from fixture.session import SessionHelper
from model.users import Users


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.payment = PaymentHelper(self)
        self.localization = LocalizationHelper(self)
        self.navigation = NavigationHelper(self)

    def destroy(self):
        self.wd.quit()
