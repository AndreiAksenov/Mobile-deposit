from selenium.webdriver.chrome.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://qa:Af4shrewyirlyuds@ibitcy.com/interview/qa/mobile-deposit/")

    def login(self, login, password):
        wd = self.wd
        wd.find_element_by_name('username').send_keys(login)
        wd.find_element_by_name('password').send_keys(password)
        wd.find_element_by_link_text('PROCEED')

    def destroy(self):
        self.wd.quit()
