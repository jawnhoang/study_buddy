import pytest
from app.models import User

@pytest.fixture(scope='module')
def new_user():
    user =User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user

def test_new_user(new_user):
    assert new_user.email =='patkennedy79@gmail.com'
    assert new_user.password_hash !='FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role =='user'