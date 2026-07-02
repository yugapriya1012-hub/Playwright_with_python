import pytest

@pytest.fixture(scope="function")
def login_page(page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield page
    page.close()