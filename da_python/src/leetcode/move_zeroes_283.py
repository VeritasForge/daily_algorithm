"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Difficulty: Easy

문제 설명:
    정수 배열 nums가 주어졌을 때, 0이 아닌 원소들의 상대적 순서를 유지하면서
    모든 0을 배열의 끝으로 이동시킨다.

    배열의 복사본을 만들지 않고 in-place로 수행해야 한다.

예시:
    Input:  nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

    Input:  nums = [0]
    Output: [0]

제약 조건:
    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1

Follow up:
    수행하는 총 연산 횟수를 최소화할 수 있는가?
"""


def move_zeroes(nums: list[int]) -> None:
    """
     Do not return anything, modify nums in-place instead.

    Two Pointer 접근:
         - write: 다음 non-zero가 들어갈 위치
         - read:  배열을 훑는 포인터
         non-zero를 만날 때마다 write 자리와 swap 후 write++
         => 0은 자연스럽게 뒤로 밀려난다.

     시간 복잡도: O(n)  - 한 번 순회
     공간 복잡도: O(1)  - in-place
     연산 횟수:   non-zero 개수만큼만 swap (Follow-up 최적화)
    """
    write = 0
    for read, n in enumerate(nums):
        if n == 0:
            continue

        nums[write], nums[read] = nums[read], nums[write]
        write += 1
