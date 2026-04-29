"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

Difficulty: Medium

문제 설명:
    m x n 격자 위에 로봇이 있습니다. 로봇은 처음에 왼쪽 위 모서리(grid[0][0])에 위치하며,
    오른쪽 아래 모서리(grid[m-1][n-1])에 도달하려고 합니다.
    로봇은 한 번에 아래(down) 또는 오른쪽(right)으로만 이동할 수 있습니다.

    두 정수 m과 n이 주어질 때, 로봇이 오른쪽 아래 모서리에 도달할 수 있는
    고유한 경로의 수를 반환하세요.

    테스트 케이스는 답이 2 * 10^9 이하가 되도록 생성됩니다.

제약 조건:
    - 1 <= m, n <= 100
"""


def unique_paths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
