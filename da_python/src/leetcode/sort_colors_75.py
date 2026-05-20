"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/

Difficulty: Medium

문제 설명:
    빨강, 흰색, 파랑으로 색칠된 n개의 객체를 가진 배열 nums가 주어집니다.
    같은 색의 객체가 인접하도록 in-place로 정렬하되, 색의 순서는
    빨강, 흰색, 파랑 순서가 되도록 하세요.

    정수 0, 1, 2는 각각 빨강, 흰색, 파랑을 나타냅니다.

    라이브러리의 정렬 함수를 사용하지 않고 풀어야 합니다.

    Example 1:
        Input:  nums = [2, 0, 2, 1, 1, 0]
        Output: [0, 0, 1, 1, 2, 2]

    Example 2:
        Input:  nums = [2, 0, 1]
        Output: [0, 1, 2]

제약 조건:
    - n == nums.length
    - 1 <= n <= 300
    - nums[i]는 0, 1, 2 중 하나

Follow up:
    상수 추가 공간만 사용하는 one-pass 알고리즘을 만들 수 있나요?
"""


# def sort_colors(nums: list[int]) -> None:
#     cnt = Counter(nums)
#     nums[:] = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]
#


# def sort_colors(nums: list[int]) -> None:
#     cnt = {0: 0, 1: 0, 2: 0}
#
#     for n in nums:
#         cnt[n] += 1
#
#     nums[:] = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]


# def sort_colors(nums: list[int]) -> None:
#     cnt = {0: 0, 1: 0, 2: 0}
#
#     for n in nums:
#         cnt[n] += 1
#
#     nums[:] = [k for k, v in cnt.items() for _ in range(v)]


# def sort_colors(nums: list[int]) -> None:
#     lo, m, hi = 0, 0, len(nums) - 1
#
#     while m <= hi:
#         if nums[m] == 0:
#             nums[lo], nums[m] = nums[m], nums[lo]
#             m += 1
#             lo += 1
#         elif nums[m] == 1:
#             m += 1
#         else:
#             nums[m], nums[hi] = nums[hi], nums[m]
#             hi -= 1


def sort_colors(nums: list[int]) -> None:
    lo, m, hi = 0, 0, len(nums) - 1
    while m <= hi:
        match nums[m]:
            case 0:
                nums[lo], nums[m] = nums[m], nums[lo]
                m += 1
                lo += 1
            case 1:
                m += 1
            case _:
                nums[m], nums[hi] = nums[hi], nums[m]
                hi -= 1
