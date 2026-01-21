"""
https://leetcode.com/problems/permutations/

46. Permutations (Medium)

문제 설명:
    주어진 고유한 정수 배열 nums에 대해 가능한 모든 순열을 반환합니다.
    순열은 어떤 순서로든 반환할 수 있습니다.

예제 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

예제 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

예제 3:
    Input: nums = [1]
    Output: [[1]]

제약 조건:
    - 1 <= nums.length <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique.
"""


# def permute(nums: list[int]) -> list[list[int]]:
#     res = []
#     def f(path, remains):
#         if not remains:
#             res.append(path[:])
#             return
#
#         for i, c in enumerate(remains):
#             path.append(c)
#             f(path, remains[:i] + remains[i+1:])
#             path.pop()
#
#     f([], nums)
#     return res


def permute(nums: list[int]) -> list[list[int]]:
    res = []

    def f(start):
        if start == len(nums):
            res.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            f(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    f(0)
    return res
