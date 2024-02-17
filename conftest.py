import pytest

from src.api_client import ApiClient


@pytest.fixture
def my_url():
    return ApiClient(base_address="https://httpbin.org/")


@pytest.fixture
def base_url():
    return "https://httpbin.org/"
