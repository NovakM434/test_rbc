from utils.api_base import Api


class RbcApi(Api):

    def __init__(self, url):
        super().__init__(url)
        self.url = url

    def get_endpoint_data(self):
        return self.get(f"{self.url}")
