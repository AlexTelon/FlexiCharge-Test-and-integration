import requests
import pytest

class TestApi:
    
    def test_api_status_code(self):
        r = requests.get("http://18.202.253.30:8080")
        assert r.status_code == 200, "Status code is not 200"
        
    def test_api_encoding(self):
        r = requests.get("http://18.202.253.30:8080")
        assert r.encoding == "utf-8", "Encoding is not utf-8"
        
        
    
