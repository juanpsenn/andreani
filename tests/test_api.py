import pytest
from andreani.core.api import SDK

def test_login_successfully(username, password, sdk):
    response = sdk.login(username, password)
    
    assert response.get("status") == 200