"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Difficulty: Medium

문제 설명:
    서로 다른 정수 배열 candidates와 목표 정수 target이 주어질 때,
    합이 target이 되는 candidates의 모든 고유한 조합을 반환하라.

    - 조합은 어떤 순서로든 반환할 수 있다.
    - 같은 숫자를 무제한으로 선택할 수 있다.
    - 두 조합이 고유하려면 선택된 숫자 중 하나 이상의 빈도가 달라야 한다.

제약 조건:
    - 1 <= candidates.length <= 30
    - 2 <= candidates[i] <= 40
    - candidates의 모든 원소는 서로 다르다
    - 1 <= target <= 40
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    합이 target이 되는 모든 고유한 조합을 반환한다.
    같은 숫자를 여러 번 사용할 수 있다.

    Args:
        candidates: 서로 다른 정수 배열
        target: 목표 합

    Returns:
        합이 target이 되는 모든 고유한 조합 리스트
    """
    sorted_candidates = sorted(candidates)
    res: list[list[int]] = []

    def backtrack(start: int, path: list[int], remain: int) -> None:
        if remain == 0:
            res.append(path[:])
            return

        for i in range(start, len(sorted_candidates)):
            if remain - sorted_candidates[i] < 0:
                break

            path.append(sorted_candidates[i])
            backtrack(i, path, remain - sorted_candidates[i])
            path.pop()

    backtrack(0, [], target)
    return res
