from moradia_ifpe.core.apps import CoreConfig


def test_app_name():
    assert CoreConfig.name == 'moradia_ifpe.core'
