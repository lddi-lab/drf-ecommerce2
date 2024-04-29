import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import CategoryFactory


register(CategoryFactory)
# register(ProductFactory)
# register(ProductLineFactory)
# register(ProductImageFactory)
# register(ProductTypeFactory)
# register(AttributeFactory)
# register(AttributeValueFactory)


@pytest.fixture
def api_client():
    return APIClient
