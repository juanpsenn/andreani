import pytest
from andreani.core.api import SDK

@pytest.fixture
def username():
    return "usuario_test"

@pytest.fixture
def password():
    return "DI$iKqMClEtM"

@pytest.fixture
def sdk():
    return SDK(sandbox=True)