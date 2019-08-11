# -*- coding: utf-8 -*-
from model.selectors import SELECTORS


def test_successful_authorization(app):
    app.navigation.open_home_page()
    app.session.login('username1@name.ru', 'pass1')
    assert app.check_exists_by_xpath(SELECTORS['STATUS PRIVILEGES DESCRIPTION'])

    app.navigation.return_to_home_page()
    app.session.login('username2@name.ru', 'pass2')
    assert app.check_exists_by_xpath(SELECTORS['STATUS PRIVILEGES DESCRIPTION'])

    app.navigation.return_to_home_page()
    app.session.login('username3@name.ru', 'pass3')
    assert app.check_exists_by_xpath(SELECTORS['STATUS PRIVILEGES DESCRIPTION'])

    app.navigation.return_to_home_page()
    app.session.login('username4@name.ru', 'pass4')
    assert app.check_exists_by_xpath(SELECTORS['STATUS PRIVILEGES DESCRIPTION'])


def test_failed_authorization(app):
    app.navigation.open_home_page()
    app.session.login('', '')
    assert app.check_exists_by_class_name('close')
    app.login_page.close_notification()

    app.session.login('username1@name.ru', '')
    assert app.check_exists_by_class_name('close')
    app.login_page.close_notification()

    app.session.login('username1@name.ru', 'pass2')
    assert app.check_exists_by_class_name('close')
    app.login_page.close_notification()








