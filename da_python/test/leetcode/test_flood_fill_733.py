import pytest

from src.leetcode.flood_fill_733 import flood_fill


@pytest.mark.parametrize(
    "image, sr, sc, color, expected",
    [
        (
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            1,
            1,
            2,
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        (
            [[0, 0, 0], [0, 0, 0]],
            0,
            0,
            0,
            [[0, 0, 0], [0, 0, 0]],
        ),
    ],
)
def test_flood_fill(
    image: list[list[int]], sr: int, sc: int, color: int, expected: list[list[int]]
) -> None:
    assert flood_fill(image, sr, sc, color) == expected
