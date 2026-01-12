import pytest

from src.leetcode.container_with_most_water_11 import max_area


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_max_area(height: list[int], expected: int):
    assert max_area(height) == expected
