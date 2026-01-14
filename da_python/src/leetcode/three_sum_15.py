"""
LeetCode 15. 3Sum
https://leetcode.com/problems/3sum/

난이도: Medium

문제 설명:
정수 배열 nums가 주어질 때, i != j, i != k, j != k이면서
nums[i] + nums[j] + nums[k] == 0인 모든 삼중쌍 [nums[i], nums[j], nums[k]]를 반환하세요.

결과에 중복된 삼중쌍이 포함되어서는 안 됩니다.

예제 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
설명:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
유일한 삼중쌍은 [-1,0,1]과 [-1,-1,2]입니다.

예제 2:
Input: nums = [0,1,1]
Output: []
설명: 합이 0이 되는 삼중쌍이 없습니다.

예제 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
설명: 유일한 삼중쌍은 [0,0,0]입니다.

제약:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums, res = sorted(nums), []

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break

        if i > 0 and nums[i - 1] == nums[i]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res
