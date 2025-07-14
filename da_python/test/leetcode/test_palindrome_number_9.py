import pytest

from src.leetcode.palindrome_number_9 import Solution


class TestTwoSum:
    @pytest.mark.parametrize(
        "x, expected",
        [
            (121, True),
            (0, True),
            (-121, False),
            (10, False),
        ],
    )
    def test_two_sum(self, x, expected):
        assert Solution().isPalindrome(x) is expected
