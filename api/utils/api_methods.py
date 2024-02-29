import time
import allure

from utils.api_base import Api


class RbcApi(Api):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    @allure.description("Получаем нужный нам тикер")
    def get_endpoint_data(self):
        current_time_unix = int(time.time())
        data = self.get(f"{self.url}/v10/ajax/key-indicator-update/?_={current_time_unix}")
        data_json = data.json()
        for item in data_json['shared_key_indicators_under_topline']:
            if item['item']['ticker'] == 'USD Нал':
                value1 = (item['item']['prepared']['value1'])
                value1 = float(value1.replace(',', '.'))
        return value1
