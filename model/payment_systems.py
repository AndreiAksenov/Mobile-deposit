

class PaymentSystems:

    def __init__(self, app):
        self.app = app
        self.list = {
            'VISA, MasterCard, Maestro': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[1]/span[2]',
            'VISA, MasterCard, Visa Electron': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[2]/span[2]',
            'VISA, MasterCard (2)': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[4]/span[2]',
            'Skrill': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[5]/span[2]',
            'Neteller': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[6]/span[2]',
            'Perfect Money': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[7]/span[2]',
            'Fasapay': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[8]/span[2]',
            'Payweb': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[9]/span[2]',
            'WebMoney': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[10]/span[2]',
            'UnionPay': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[11]/span[2]',
            'UnionPay 2': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[12]/span[2]',
            'QIWI': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[13]/span[2]',
            'Яндекс.Деньги': '//*[@id="riot-app"]/div/payment-system-selector/div/div[2]/rg-select/ul/li[14]/span[2]'
        }
