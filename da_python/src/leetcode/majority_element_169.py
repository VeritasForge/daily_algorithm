# https://leetcode.com/problems/majority-element/
# 169. Majority Element
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
#   Input: nums = [3,2,3]
#   Output: 3
#
# Example 2:
#   Input: nums = [2,2,1,1,1,2,2]
#   Output: 2
#
# Constraints:
#   - n == nums.length
#   - 1 <= n <= 5 * 10^4
#   - -10^9 <= nums[i] <= 10^9

from collections import Counter


def majority_element(nums: list[int]) -> int:
    # return _using_counter(nums)
    # return _using_sorting(nums)
    return _using_boyer_moore_voting_algorithm(nums)


def _using_counter(nums: list[int]) -> int:
    threshold = len(nums) // 2
    return next(n for n, c in Counter(nums).items() if c > threshold)


def _using_sorting(nums: list[int]) -> int:
    """
    정렬 (O(n log n) 시간, O(1) 공간)
    과반수 원소는 정렬 후 항상 중앙에 위치
    """
    return sorted(nums)[len(nums) // 2]


def _using_boyer_moore_voting_algorithm(nums: list[int]) -> int:
    """
    Boyer-Moore Voting Algorithm
    과반수 원소는 다른 모든 원소와 1:1로 상쇄해도 반드시 남는다.
    """
    candidate = 0
    count = 0

    for n in nums:
        if count == 0:
            candidate = n

        count += 1 if candidate == n else -1

    return candidate
