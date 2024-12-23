import pytest
import requests

from tests.schemas import companies_schema

@pytest.mark.api
@pytest.mark.getMethod
def test_getMethod(base_url):
    """Test case: get all companies"""
    response=requests.get(base_url)
    assert response.status_code == 200, "Status code response is not successful"
    assert companies_schema == response.json(), "Incorrect response schema"