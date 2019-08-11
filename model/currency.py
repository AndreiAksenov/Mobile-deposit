

class Currency:

    def __init__(self, app):
        self.app = app
        self.usd = {
            'mini': 400,
            'silver': 1000,
            'gold': 2000,
            'vip': 5000,
        }
        self.rub = {
            'mini': 20000,
            'silver': 50000,
            'gold': 100000,
            'vip': 400000,
        }
        self.cnh = {
            'mini': 3376,
            'silver': 5776,
            'gold': 13776,
            'vip': 37776,
        }
