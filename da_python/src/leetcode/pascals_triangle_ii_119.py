"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Difficulty: Easy

문제 설명:
    정수 rowIndex가 주어질 때, 파스칼의 삼각형의 rowIndex번째 (0-indexed) 행을 반환하라.
    파스칼의 삼각형에서 각 숫자는 바로 위에 있는 두 숫자의 합이다.

제약 조건:
    0 <= rowIndex <= 33

Follow up:
    O(rowIndex) 만큼의 추가 공간만 사용하도록 최적화할 수 있는가?
"""


def get_row(row_index: int) -> list[int]:
    res = [1]
    for _ in range(row_index):
        res = [a + b for a, b in zip([0] + res, res + [0])]
    return res
