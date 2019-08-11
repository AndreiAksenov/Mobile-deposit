

class LocalizationHelper:

    def __init__(self, app):
        self.app = app

    def change(self, localization):
        wd = self.app.wd
        wd.find_element_by_link_text(localization).click()

    def param_from_url(self):
        wd = self.app.wd
        url = wd.current_url
        new_url = str(url).split('lang=')
        return new_url[1][:2]
