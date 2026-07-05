"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Difficulty: Easy

문제 설명:
    정수 numRows가 주어질 때, 파스칼의 삼각형의 첫 numRows개 행을 반환하라.
    파스칼의 삼각형에서 각 숫자는 바로 위에 있는 두 숫자의 합이다.

제약 조건:
    1 <= numRows <= 30
"""


def generate(num_rows: int) -> list[list[int]]:
    res = [[1]]

    for _ in range(num_rows - 1):
        prev = res[-1]
        curr = [a + b for a, b in zip([0] + prev, prev + [0])]
        res.append(curr)

    return res


# def generate(num_rows: int) -> list[list[int]]:
#     res = [[1]]
#     for _ in range(num_rows - 1):
#         prev, curr = res[-1], []
#         for i in range(len(prev) + 1):
#             if i == 0 or i == len(prev):
#                 curr.append(1)
#             else:
#                 curr.append(prev[i - 1] + prev[i])
#         res.append(curr)
#     return res
