#package->Every folder/package
import pytest

@pytest.fixture(scope="package")
def setup():
    print("Package Setup")
    yield
    print("Package Teardown")