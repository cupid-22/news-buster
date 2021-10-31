import requests


class API:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, domain_url, payload):
        response = requests.post(f'{self.base_url}/{domain_url}', timeout=20, params=payload)
        response.raise_for_status()
        return response

    def get(self, domain_url, get_params):
        response = requests.get(f'{self.base_url}/{domain_url}', timeout=10, params=get_params)
        response.raise_for_status()
        return response
