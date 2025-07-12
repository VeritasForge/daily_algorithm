from src.leetcode.two_sum_1 import Solution

class TestTwoSum:
    def test_two_sum(self):
        solution = Solution()
        assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
        assert solution.twoSum([3, 2, 4], 6) == [1, 2]
        assert solution.twoSum([3, 3], 6) == [0, 1]