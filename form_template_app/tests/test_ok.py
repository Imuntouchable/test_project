import pytest
from rest_framework.test import APIClient

from .constants import URL


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_get_form(api_client):
    """Пример теста с корректным запросом."""
    data = [{
        'field_customer_phone': '+7 999 999 99 99',
        'field_date': '2004-12-14',
        'field_comments': 'text'
    }]
    response = api_client.post(URL, data, format='json')
    assert response.status_code == 200
    assert response.data['template_name'] == 'Comments Form'
