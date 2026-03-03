import pytest

from src.leetcode.combinations_77 import combine


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (1, 1, [[1]]),
    ],
)
def test_combine(n: int, k: int, expected: list[list[int]]) -> None:
    result = combine(n, k)
    # 순서에 상관없이 비교
    assert sorted([sorted(combo) for combo in result]) == sorted(
        [sorted(combo) for combo in expected]
    )
