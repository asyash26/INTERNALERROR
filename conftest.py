import pytest
import pytest_check


@pytest.fixture(name="my_fixture", scope="session")
def my_fixture() -> int:
    try:
        yield 1
    finally:
        pytest_check.fail("Fail error message")
