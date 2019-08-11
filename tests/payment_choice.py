import time

def test_select_status_privileges(app):
    app.navigation.open_home_page()
    app.session.login('username1@name.ru', 'pass1')

    app.payment.select_currency('USD')
    app.payment.select_status('mini')
    assert app.payment.get_amount('USD') == app.currency.usd['mini']
    app.payment.select_status('silver')
    assert app.payment.get_amount('USD') == app.currency.usd['silver']
    app.payment.select_status('gold')
    assert app.payment.get_amount('USD') == app.currency.usd['gold']
    app.payment.select_status('vip')
    assert app.payment.get_amount('USD') == app.currency.usd['vip']

    app.payment.select_currency('RUB')
    app.payment.select_status('mini')
    assert app.payment.get_amount('RUB') == app.currency.rub['mini']
    app.payment.select_status('silver')
    assert app.payment.get_amount('RUB') == app.currency.rub['silver']
    app.payment.select_status('gold')
    assert app.payment.get_amount('RUB') == app.currency.rub['gold']
    app.payment.select_status('vip')
    assert app.payment.get_amount('RUB') == app.currency.rub['vip']

    app.payment.select_currency('CNH')
    app.payment.select_status('mini')
    assert app.payment.get_amount('CNH') == app.currency.cnh['mini']
    app.payment.select_status('silver')
    assert app.payment.get_amount('CNH') == app.currency.cnh['silver']
    app.payment.select_status('gold')
    assert app.payment.get_amount('CNH') == app.currency.cnh['gold']
    app.payment.select_status('vip')
    assert app.payment.get_amount('CNH') == app.currency.cnh['vip']


def test_select_payment_system(app):
    app.navigation.open_home_page()
    app.session.login('username1@name.ru', 'pass1')
    app.payment.open_payment_system_page()

    for key, value in app.payment_systems.list.items():
        app.payment.select_payment_system(value)
        time.sleep(0.1)
        assert app.payment.selected_payment_system() == key
        app.payment.open_payment_system_page()
