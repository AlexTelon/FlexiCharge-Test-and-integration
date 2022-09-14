import requests
import pytest

class TestApi:
    
    def test_api(self):
        r = requests.get("http://18.202.253.30:8080")
        assert r.status_code == 200