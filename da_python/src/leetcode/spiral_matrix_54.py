"""
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Difficulty: Medium

문제 설명:
    m x n 행렬이 주어질 때, 행렬의 모든 원소를 나선형(spiral) 순서로 반환하라.

제약 조건:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 10
    - -100 <= matrix[i][j] <= 100
"""


def spiral_order(matrix: list[list[int]]) -> list[int]:
    res: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            res.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            res.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

    return res


# def spiral_order(matrix: list[list[int]]) -> list[int]:
#     res: list[int] = []
#     top, bottom = 0, len(matrix) - 1
#     left, right = 0, len(matrix[0]) - 1
#
#     while top <= bottom and left <= right:
#         # → 오른쪽: top 행을 left에서 right까지
#         for col in range(left, right + 1):
#             res.append(matrix[top][col])
#         top += 1
#
#         # ↓ 아래: right 열을 top에서 bottom까지
#         for row in range(top, bottom + 1):
#             res.append(matrix[row][right])
#         right -= 1
#
#         # ← 왼쪽: bottom 행을 right에서 left까지 (행이 남아있을 때만)
#         if top <= bottom:
#             for col in range(right, left - 1, -1):
#                 res.append(matrix[bottom][col])
#             bottom -= 1
#
#         # ↑ 위: left 열을 bottom에서 top까지 (열이 남아있을 때만)
#         if left <= right:
#             for row in range(bottom, top - 1, -1):
#                 res.append(matrix[row][left])
#             left += 1
#
#     return res
