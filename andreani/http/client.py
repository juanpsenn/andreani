import requests
from requests.auth import HTTPBasicAuth


class HttpClient:
    """Basic HTTP client"""

    def request(self, method, url=None, params=None, **kwargs):
        api_result = requests.request(method, url, params=params, **kwargs)
        response = {"status": api_result.status_code, "response": api_result.json()}
        return response

    def get(self, url=None, params=None, **kwargs):
        return self.request("GET", url, params=params, **kwargs)

    def post(self):
        return self.request("POST", url=None, params=None, **kwargs)

    def put(self):
        return self.request("PUT", url, params, **kwargs)

    def delete(self):
        return self.request("DELETE", url=None, params=None, **kwargs)
