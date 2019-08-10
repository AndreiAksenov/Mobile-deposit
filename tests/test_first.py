# -*- coding: utf-8 -*-
from app_manager.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_first(app):
    app.open_home_page()
    app.login('username1@name.ru', 'pass1')



