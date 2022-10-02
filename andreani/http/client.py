import requests
from requests.auth import HTTPBasicAuth

class HttpClient:
    """ Basic HTTP client """

    def request(self, method, url, params, **kwargs):
        api_result = requests.request(method, url, **kwargs)
        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }
        return response
    
    def get(self, method, url, params, **kwargs):
        return self.request("GET", url, params, **kwargs)

    def post(self):
        return self.request("POST", url, params, **kwargs)
        
    def put(self):
        return self.request("PUT", url, params, **kwargs)
        
    def delete(self):
        return self.request("DELETE", url, params, **kwargs)
        