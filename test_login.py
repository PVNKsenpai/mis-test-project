import pytest
from src.sample_mis_code import MIS

def test_login_success():
    system = MIS()
    assert system.login("admin", "123456") is True

def test_login_fail():
    system = MIS()
    assert system.login("user", "wrong") is False
