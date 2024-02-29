import pytest
import allure

from utils.helpers import check_condition

class TestRbcEndpoint:

    @pytest.mark.endpoint
    @allure.title("Проверка тикера 'USD Нал'")
    @allure.description("Тест проверяет что тикер USD Нал находится диапазоне от 60 до 120")
    def test_endpoint(self, api):
        data = api.get_endpoint_data()
        check_condition(60 <= data <= 120, f"Значение value1 для USD Нал должно быть между 60 и 120")
