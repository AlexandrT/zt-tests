import json

import pytest
import requests
from random import randrange
from lib.config import settings


@pytest.fixture(scope="function")
def not_existed_login():
    res = requests.get(settings.DATA_URL)
    json_data = json.loads(res.text)
    return json_data[randrange(5)]["email"]


@pytest.fixture()
def phone():
    return settings.PHONE


@pytest.fixture()
def phone_code():
    return settings.PHONE_CODE
