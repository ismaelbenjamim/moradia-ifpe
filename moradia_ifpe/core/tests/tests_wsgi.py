import os

from django.core.handlers.wsgi import WSGIHandler

from moradia_ifpe.wsgi import application


def test_wsgi_default_settings():
    assert 'moradia_ifpe.settings' == os.environ["DJANGO_SETTINGS_MODULE"]


def test_application_instance():
    assert isinstance(application, WSGIHandler)
