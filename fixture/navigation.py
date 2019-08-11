

class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://qa:Af4shrewyirlyuds@ibitcy.com/interview/qa/mobile-deposit/")

    def return_to_home_page(self):
        wd = self.app.wd
        wd.get("https://ibitcy.com/interview/qa/mobile-deposit/")
