from .constants import BASE_URLS as URLS
from andreani.http.client import HttpClient
from requests.auth import HTTPBasicAuth
import typing

class SDK:  
    sandbox: bool
    url: str

    def __init__(self, sandbox=False):
        self.sandbox = sandbox
        self.url = URLS["test"] if sandbox else URLS["prod"]
        self.http_client = HttpClient()

    def login(self, username: str, password: str) -> typing.Optional[str]:
        endpoint = self.url + "/login"
        response = self.http_client.get(url=endpoint, auth=HTTPBasicAuth(username, password))
        if response.get("status") == 200:
            return response.get("response")["token"]
        return None

