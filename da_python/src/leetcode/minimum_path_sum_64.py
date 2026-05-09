"""
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Difficulty: Medium

문제 설명:
    m x n 그리드가 음이 아닌 정수로 채워져 있을 때,
    왼쪽 상단에서 오른쪽 하단까지의 경로 중 경로 위 숫자의 합이
    최소가 되는 경로를 찾아 그 합을 반환하라.
    이동은 오른쪽 또는 아래쪽으로만 가능하다.

제약 조건:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 200
    - 0 <= grid[i][j] <= 200
"""


def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            if i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[m - 1][n - 1]


# def min_path_sum(grid: list[list[int]]) -> int:
#     m, n = len(grid), len(grid[0])
#
#     for i in range(m):
#         for j in range(n):
#             match (i, j):
#                 case (0, 0):
#                     continue
#                 case (0, _):
#                     grid[i][j] += grid[i][j - 1]
#                 case (_, 0):
#                     grid[i][j] += grid[i - 1][j]
#                 case _:
#                     grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
#
#     return grid[m - 1][n - 1]
