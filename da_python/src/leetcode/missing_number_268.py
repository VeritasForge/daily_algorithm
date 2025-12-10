# https://leetcode.com/problems/missing-number/
# 268. Missing Number
#
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
#
# Example 1:
#   Input: nums = [3,0,1]
#   Output: 2
#   Explanation: n = 3 since there are 3 numbers, so all numbers are in
#   the range [0,3]. 2 is the missing number in the range since it does
#   not appear in nums.
#
# Example 2:
#   Input: nums = [0,1]
#   Output: 2
#   Explanation: n = 2 since there are 2 numbers, so all numbers are in
#   the range [0,2]. 2 is the missing number in the range since it does
#   not appear in nums.
#
# Example 3:
#   Input: nums = [9,6,4,2,3,5,7,0,1]
#   Output: 8
#   Explanation: n = 9 since there are 9 numbers, so all numbers are in
#   the range [0,9]. 8 is the missing number in the range since it does
#   not appear in nums.
#
# Constraints:
#   - n == nums.length
#   - 1 <= n <= 10^4
#   - 0 <= nums[i] <= n
#   - All the numbers of nums are unique.
#
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?


# def missing_number(nums: list[int]) -> int:
#     candidate = 0
#     for n in sorted(nums):
#         if n != candidate:
#             return candidate
#         candidate += 1
#
#     return candidate

# def missing_number(nums: list[int]) -> int:
#     num_set = set(nums)
#     for i in range(len(num_set)):
#         if i not in num_set:
#             return i
#     return len(num_set)


# def missing_number(nums: list[int]) -> int:
#     """
#     ⏺ Gauss 공식 (등차수열의 합)
#
#       공식: 1부터 n까지의 합 = n * (n + 1) / 2
#
#       ---
#       유래
#
#       독일 수학자 가우스(Carl Friedrich Gauss)가 초등학생 때 선생님이 "1부터 100까지 더해라"라는 문제를 냈는데, 몇
#       초 만에 5050이라고 답했다는 일화에서 유명해졌습니다.
#
#       ---
#       원리
#
#       1부터 n까지 두 번 나열하고, 하나는 역순으로 배치:
#
#         1 +  2 +  3 + ... + n
#       + n + n-1 + n-2 + ... + 1
#       ─────────────────────────
#       (n+1) + (n+1) + (n+1) + ... + (n+1)  ← n개
#
#       각 쌍의 합이 (n+1)이고, 이런 쌍이 n개 → 총합은 n * (n+1)
#
#       하지만 두 번 더했으므로 2로 나누면: n * (n + 1) / 2
#
#       ---
#       활용 사례
#
#       | 상황             | 적용                                     |
#       |----------------|----------------------------------------|
#       | Missing Number | 기대 합 - 실제 합 = 빠진 숫자                    |
#       | 배열 인덱스 합       | 0~n-1 인덱스의 총합 계산                       |
#       | 페이지네이션         | 1~n페이지까지 총 아이템 수                       |
#       | 삼각수            | n번째 삼각수 = 1+2+...+n                    |
#       | 시간 복잡도 분석      | 이중 루프 for i: for j in range(i) → O(n²) |
#
#       ---
#       0부터 시작하는 경우
#
#       이 문제는 0부터 n까지이므로:
#       0 + 1 + 2 + ... + n = n * (n + 1) / 2
#       (0을 더해도 합은 같음)
#     """
#     n = len(nums)
#     return (n + 1) * n // 2 - sum(nums)


def missing_number(nums: list[int]) -> int:
    result = len(nums)
    for i, n in enumerate(nums):
        result ^= i ^ n
    return result
