import pytest
from login_page import LoginPage
from csv_reader import get_login_data

# @pytest.mark.parametrize("data",get_login_data())
# def test_login(data):
#     print(data["username"])
#     print(data["password"])

@pytest.mark.parametrize("data",get_login_data())
def test_login(page,data):
    login=LoginPage(page)
    login.open()
    login.login(
    data["username"],
    data["password"]
    )
