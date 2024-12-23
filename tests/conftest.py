import pytest

@pytest.fixture()
def base_url():
    """Ficture to set the base url"""
    return "https://fake-json-api.mock.beeceptor.com/companies"