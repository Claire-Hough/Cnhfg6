import pytest

from mycode.login import login

def test_successful_login():
    """
    The Admin user can login with a password value of 'password'
    """
    assert login( 'admin', 'password' ) == True

def test_failed_login():
    """
    The Admin user login will fail with an invalid password
    """
    assert login( 'admin', 'foo' ) == False
