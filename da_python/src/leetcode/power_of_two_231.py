"""
231. Power of Two
https://leetcode.com/problems/power-of-two/

Difficulty: Easy

문제 설명:
    정수 n이 주어졌을 때, n이 2의 거듭제곱이면 true를, 아니면 false를 반환하라.
    정수 n이 2의 거듭제곱이란, n == 2^x를 만족하는 정수 x가 존재하는 것을 의미한다.

제약 조건:
    -2^31 <= n <= 2^31 - 1

Follow up:
    반복문/재귀 없이 풀 수 있는가?
"""


def is_power_of_two(n: int) -> bool:
    return n > 0 and not (n & (n - 1))
