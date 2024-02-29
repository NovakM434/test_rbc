import requests


class Api:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(endpoint)
