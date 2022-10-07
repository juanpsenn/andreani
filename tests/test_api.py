import pytest
from andreani.core.api import SDK

def test_login_successfully(username, password, sdk):
    response = sdk.login(username, password)
    
    assert response is not None
    assert type(response) == str