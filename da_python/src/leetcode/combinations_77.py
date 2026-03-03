"""
77. Combinations
https://leetcode.com/problems/combinations/

Difficulty: Medium

문제 설명:
    두 정수 n과 k가 주어질 때, [1, n] 범위에서 k개의 숫자를 선택하는
    모든 가능한 조합을 반환하라.

    결과는 어떤 순서로든 반환할 수 있다.

제약 조건:
    - 1 <= n <= 20
    - 1 <= k <= n
"""


def combine(n: int, k: int) -> list[list[int]]:
    """
    [1, n] 범위에서 k개를 선택하는 모든 조합을 반환한다.

    Args:
        n: 범위의 최댓값 (1부터 n까지)
        k: 선택할 숫자의 개수

    Returns:
        가능한 모든 조합의 리스트
    """
    res = []

    def f(start, comb):
        if len(comb) == k:
            res.append(comb[:])
            return

        for v in range(start, n + 1):
            comb.append(v)
            f(v + 1, comb)
            comb.pop()

    f(1, [])
    return res
