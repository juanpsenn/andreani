from .constants import BASE_URLS as URLS
from andreani.http.client import HttpClient
from requests.auth import HTTPBasicAuth

class SDK:  
    sandbox: bool
    url: str

    def __init__(self, sandbox=False):
        self.sandbox = sandbox
        self.url = URLS["test"] if sandbox else URLS["prod"]
        self.http_client = HttpClient()

    def login(self, username: str, password: str) -> str:
        endpoint = self.url + "/login"
        response = self.http_client.get(url=endpoint, auth=HTTPBasicAuth(username, password))
        return response


