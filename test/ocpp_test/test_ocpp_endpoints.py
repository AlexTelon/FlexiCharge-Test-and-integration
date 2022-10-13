from urllib import response
import requests
import pytest

OCPP_TESTING_API_URL = "http://localhost:8080/tests/ocpp"

class TestOcppEndpoints:
    
    def test_ocpp_endpoints_code():
        r = requests.get(OCPP_TESTING_API_URL)
        assert r.json()["failedTests"] == [], r.json()["failedTests"]

TestOcppEndpoints.test_ocpp_endpoints_code()
