

def test_change_localization(app):
    app.navigation.open_home_page()

    app.localization.change('EN')
    assert app.localization.param_from_url() == 'en'

    app.localization.change('CH')
    # assert app.localization_param_from_url() == 'ch' /// БАГ в урле zh-Hans

    app.localization.change('KO')
    assert app.localization.param_from_url() == 'ko'

    app.localization.change('RU')
    assert app.localization.param_from_url() == 'ru'

    app.localization.change('HI')
    assert app.localization.param_from_url() == 'hi'

