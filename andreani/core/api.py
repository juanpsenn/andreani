from .constants import URLS
from http.client import HttpClient

class SDK:  
    sandbox: bool
    url: str

    def __init__(self, sandbox=False):
        self.sandbox = sandbox
        self.url = URLS["test"] if sandbox else URLS["prod"]
        self.http_client = HttpClient()

    def login(username: str, password: str) -> str:
        endpoint = self.url + "/login"
        try:
            response = self.http_client.get(endpoint, auth=HTTPBasicAuth(username, password))
            return response.json()["token"]
        except Exception as exc:
            return None

