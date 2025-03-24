import pytest


@pytest.mark.skip
def test_my_fixture(
        my_fixture
) -> None:
    assert my_fixture == 2, "Unexpected failure"
