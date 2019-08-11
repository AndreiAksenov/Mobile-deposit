

def test_successful_repair_password(app):
    app.navigation.open_home_page()
    app.login_page.repair_password('username1@name.ru')
    assert app.check_exists_by_class_name('close')
    app.login_page.close_notification()


def test_failed_repair_password(app):
    app.navigation.open_home_page()
    app.login_page.repair_password('nonexistent@name.ru')
    assert app.check_exists_by_class_name('close') is False

    app.navigation.open_home_page()
    app.login_page.repair_password('')
    assert app.check_exists_by_class_name('close') is False





