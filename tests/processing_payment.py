import time
import random
import secrets


def test_processing_payment(app):
    currency = ['USD', 'RUB', 'CNH']
    status_privileges = ['mini', 'silver', 'gold', 'vip']

    app.navigation.open_home_page()
    app.session.login('username1@name.ru', 'pass1')
    app.payment.open_payment_system_page()

    for key, value in app.payment_systems.list.items():
        app.payment.select_payment_system(value)
        time.sleep(0.1)
        assert app.payment.selected_payment_system() == key
        time.sleep(0.1)
        rand_currency = random.choice(currency)
        app.payment.select_currency(rand_currency)
        time.sleep(0.1)
        rand_status_privileges = random.choice(status_privileges)
        app.payment.select_status(rand_status_privileges)
        time.sleep(0.1)
        app.payment.apply()
        if rand_currency == 'KIWI':
            #нужно дописать
            pass
        else:
            assert app.check_exists_by_css_selector('#riot-app .deposit-result.result .icon')
            app.payment.back_to()
        app.payment.open_payment_system_page()

