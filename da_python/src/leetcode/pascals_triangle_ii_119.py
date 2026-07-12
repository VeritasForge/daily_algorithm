"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Difficulty: Easy

문제 설명:
    정수 row_index가 주어질 때, 파스칼의 삼각형의 row_index번째 (0-indexed) 행을 반환하라.
    파스칼의 삼각형에서 각 숫자는 바로 위에 있는 두 숫자의 합이다.

제약 조건:
    0 <= rowIndex <= 33

Follow up:
    O(row_index) 만큼의 추가 공간만 사용하도록 최적화할 수 있는가?
"""


# def get_row(row_index: int) -> list[int]:
#     res = [1]
#     for _ in range(row_index):
#         res = [a + b for a, b in zip([0] + res, res + [0])]
#     return res

def get_row(row_index: int) -> list[int]:
    row = [1]
    for i in range(1, row_index + 1):
        row.append(row[i - 1] * (row_index - i + 1) // i)
    return row
