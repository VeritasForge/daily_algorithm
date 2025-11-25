"""
https://leetcode.com/problems/single-number/

136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

# def single_number(nums: list[int]) -> int:
#     counter: dict[int, int] = {}
#
#     for n in nums:
#         counter[n] = counter.get(n, 0) + 1
#
#     return next(n for n, c in counter.items() if c == 1)


# def single_number(nums: list[int]) -> int:
#     counter = Counter(nums)
#     return next(n for n, cnt in counter.items() if cnt == 1)


def single_number(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res
