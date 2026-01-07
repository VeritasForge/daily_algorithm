# https://leetcode.com/problems/contains-duplicate
# 217. Contains Duplicate
# Easy
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.


# def contains_duplicate(nums: list[int]) -> bool:
#     return len(set(nums)) != len(nums)


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
