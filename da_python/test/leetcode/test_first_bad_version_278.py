import pytest

from src.leetcode.first_bad_version_278 import first_bad_version


def make_is_bad_version(bad: int):
    """Create an isBadVersion function for testing."""

    def is_bad_version(version: int) -> bool:
        return version >= bad

    return is_bad_version


@pytest.mark.parametrize(
    "n, bad",
    [
        (5, 4),
        (1, 1),
        (5, 1),
        (5, 5),
        (10, 7),
    ],
)
def test_first_bad_version(n: int, bad: int):
    assert first_bad_version(n, make_is_bad_version(bad)) == bad
