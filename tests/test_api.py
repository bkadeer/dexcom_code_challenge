from utils.data import TestData as td
import requests
import pytest_check as check


def test_validate_200():
    status = requests.get(td.BASE_URL)
    check.equal(200, status.status_code)
