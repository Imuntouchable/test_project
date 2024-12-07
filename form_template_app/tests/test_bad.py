import pytest
from rest_framework.test import APIClient

from .constants import URL


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_get_form_invalid(api_client):
    """Пример теста с ошибочным запросом."""
    data = [{
        'field_customer_phone': 'invalid phone',
        'field_date': 'invalid date',
        'field_comments': 'text'
    }]
    response = api_client.post(URL, data, format='json')
    assert response.status_code == 404
    assert 'field_customer_phone' in response.data
    assert 'field_date' in response.data
