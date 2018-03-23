import pytest

from cylon import Cylon


@pytest.fixture
def cylon_models():
    # source: https://en.battlestarwikiclone.org/wiki/Cylon_Models
    models = [
        'U-87 Cyber Combat Unit',
        'Civilian Cylon',
        'Cylon War-Era Centurion',
        'Cython',
        'Djerba Centurion',
        'Modern Centurion',
        'Inorganic Humanoids',
        'Cylon Spacecraft',
        'Cylon Hybrids',
        'Humanoid Cylons',
    ]
    return Cylon(models)


def test_cylon_object(cylon_models):
    assert isinstance(cylon_models, Cylon)
    assert repr(cylon_models) == '<Cylon items=10 index=0>'
    assert str(cylon_models) == 'U-87 Cyber Combat Unit'


def test_cylon_defaults(cylon_models):
    assert cylon_models.count == 10
    assert cylon_models.index == 0
    assert cylon_models.current == 'U-87 Cyber Combat Unit'


def test_cylon_methods(cylon_models):
    assert cylon_models.next() == 'Civilian Cylon'
    assert cylon_models.index == 1
    assert cylon_models.next() == 'Cylon War-Era Centurion'
    assert cylon_models.index == 2
    assert cylon_models.next() == 'Cython'
    assert cylon_models.index == 3
    assert cylon_models.prev() == 'Cylon War-Era Centurion'
    assert cylon_models.index == 2


def test_cylon_boundaries(cylon_models):
    assert cylon_models.current == 'U-87 Cyber Combat Unit'
    assert cylon_models.index == 0
    assert cylon_models.prev() == 'Humanoid Cylons'
    assert cylon_models.index == 9
    assert cylon_models.next() == 'U-87 Cyber Combat Unit'
    assert cylon_models.index == 0
