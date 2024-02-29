import pytest
import time

from utils.api_methods import RbcApi

current_time_unix = int(time.time())

@pytest.fixture(scope="function")
def api():
    return RbcApi(f'https://www.rbc.ru/v10/ajax/key-indicator-update/?_={current_time_unix}')
