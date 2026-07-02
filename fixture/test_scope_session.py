#session ->Entire test run one
import pytest

@pytest.fixture(scope="session")
def setup():
    print("Setup")
    yield
    print("Teardown")