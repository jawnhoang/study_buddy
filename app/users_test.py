import pytest
from app.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(username='daile', email='patkennedy79@gmail.com')
    return user


def test_new_user(new_user):
    assert new_user.username == 'daile'
    assert new_user.email == 'patkennedy79@gmail.com'








