import pytest
from app.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(password_hash='Mypassword')
    return user

def test_setting_password(new_user):
    assert new_user.password_hash == "Mypassword"
