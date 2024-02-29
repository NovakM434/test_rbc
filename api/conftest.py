import pytest

from utils.api_methods import RbcApi


@pytest.fixture(scope="function")
def api():
    return RbcApi('https://www.rbc.ru/')
