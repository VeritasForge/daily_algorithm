import pytest

from src.leetcode.remove_duplicates_from_sorted_array_26 import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ],
)
def test_remove_duplicates(nums: list[int], expected: list[int]):
    # When:
    k = remove_duplicates(nums)

    # Then: 중복을 제거한 nums의 길이 검증
    assert len(expected) == k

    # And: 중복을 in-place로 제거한 nums의 데이터 검증
    assert nums == expected
