# -*- coding: utf-8 -*-


def test_successful_authorization(app):
    app.navigation.open_home_page()
    app.session.login('username1@name.ru', 'pass1')
    assert app.payment.title() == 'STATUS PRIVILEGES DESCRIPTION'

    app.navigation.return_to_home_page()
    app.session.login('username2@name.ru', 'pass2')
    assert app.payment.title() == 'STATUS PRIVILEGES DESCRIPTION'

    app.navigation.return_to_home_page()
    app.session.login('username3@name.ru', 'pass3')
    assert app.payment.title() == 'STATUS PRIVILEGES DESCRIPTION'

    app.navigation.return_to_home_page()
    app.session.login('username4@name.ru', 'pass4')
    assert app.payment.title() == 'STATUS PRIVILEGES DESCRIPTION'


def test_failed_authorization(app):
    app.navigation.open_home_page()
    app.session.login('', '')




