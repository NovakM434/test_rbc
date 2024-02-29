import pytest
import allure


class TestRbcEndpoint:

    @pytest.mark.endpoint
    @allure.title("Проверка тикера 'USD Нал'")
    @allure.description("Тест проверяет что тикер USD Нал находится диапазоне от 60 до 120")
    def test_endpoint(self, api):
        data = api.get_endpoint_data()
        json_data = data.json()
        for item in json_data['shared_key_indicators_under_topline']:
            if item['item']['ticker'] == 'USD Нал':
                value1 = (item['item']['prepared']['value1'])
                value1 = float(value1.replace(',', '.'))
                assert 60 <= value1 <= 120, f"Значение value1 для USD Нал должно быть между 60 и 120, а не {value1}"
