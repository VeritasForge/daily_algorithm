import pytest

from src.leetcode.accounts_merge_721 import accounts_merge

pytestmark = pytest.mark.skip(reason="WIP")


def _sort_by_account(result: list[list[str]]) -> list[list[str]]:
    """계정 순서만 정렬 (계정 간 순서는 상관없으므로)."""
    return sorted(result)


def _emails_are_sorted(result: list[list[str]]) -> bool:
    """각 계정의 이메일이 정렬되어 있는지 검증."""
    return all(account[1:] == sorted(account[1:]) for account in result)


@pytest.mark.parametrize(
    "accounts, expected",
    [
        # LeetCode 기본 예제
        # (
        #     [
        #         ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        #         ["John", "johnsmith@mail.com", "john00@mail.com"],
        #         ["Mary", "mary@mail.com"],
        #         ["John", "johnnybravo@mail.com"],
        #     ],
        #     [
        #         [
        #             "John",
        #             "john00@mail.com",
        #             "john_newyork@mail.com",
        #             "johnsmith@mail.com",
        #         ],
        #         ["Mary", "mary@mail.com"],
        #         ["John", "johnnybravo@mail.com"],
        #     ],
        # ),
        # (
        #     [
        #         ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        #         ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
        #         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        #         ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        #         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        #     ],
        #     [
        #         ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
        #         ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        #         ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
        #         ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
        #         ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        #     ],
        # ),
        # # 보강 - 엣지 케이스: 계정 1개
        # (
        #     [["Alice", "alice@mail.com"]],
        #     [["Alice", "alice@mail.com"]],
        # ),
        # # 보강 - 체인 병합 (A-B, B-C → A,B,C 모두 같은 사람)
        # (
        #     [
        #         ["David", "a@m.co", "b@m.co"],
        #         ["David", "b@m.co", "c@m.co"],
        #         ["David", "c@m.co", "d@m.co"],
        #     ],
        #     [
        #         ["David", "a@m.co", "b@m.co", "c@m.co", "d@m.co"],
        #     ],
        # ),
        # # 보강 - 같은 이름이지만 다른 사람 (이메일 겹침 없음)
        # (
        #     [
        #         ["Alex", "alex1@m.co"],
        #         ["Alex", "alex2@m.co"],
        #     ],
        #     [
        #         ["Alex", "alex1@m.co"],
        #         ["Alex", "alex2@m.co"],
        #     ],
        # ),
        # # 보강 - 계정 하나에 이메일이 하나만 있는 경우
        # (
        #     [
        #         ["Bob", "bob@m.co"],
        #         ["Bob", "bob@m.co", "bob2@m.co"],
        #     ],
        #     [
        #         ["Bob", "bob2@m.co", "bob@m.co"],
        #     ],
        # ),
        # # 보강 - 모든 계정이 하나로 병합
        # (
        #     [
        #         ["Eve", "a@m.co", "b@m.co"],
        #         ["Eve", "b@m.co", "c@m.co"],
        #         ["Eve", "c@m.co", "a@m.co"],
        #     ],
        #     [
        #         ["Eve", "a@m.co", "b@m.co", "c@m.co"],
        #     ],
        # ),
        # (
        #     [
        #         ["David", "David0@m.co", "David1@m.co"],
        #         ["David", "David3@m.co", "David4@m.co"],
        #         ["David", "David4@m.co", "David5@m.co"],
        #         ["David", "David2@m.co", "David3@m.co"],
        #         ["David", "David1@m.co", "David2@m.co"],
        #     ],
        #     [
        #         [
        #             "David",
        #             "David0@m.co",
        #             "David1@m.co",
        #             "David2@m.co",
        #             "David3@m.co",
        #             "David4@m.co",
        #             "David5@m.co",
        #         ]
        #     ],
        # ),
        # (
        #     [
        #         ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
        #         ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
        #         ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
        #         ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
        #         ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"],
        #     ],
        #     [
        #         ["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"],
        #         ["Ethan", "Ethan0@m.co", "Ethan3@m.co"],
        #         ["Gabe", "Gabe0@m.co", "Gabe2@m.co", "Gabe3@m.co", "Gabe4@m.co"],
        #         ["Kevin", "Kevin2@m.co", "Kevin4@m.co"],
        #     ],
        # ),
        (
            [
                ["Lily", "Lily4@m.co", "Lily5@m.co"],
                ["Lily", "Lily8@m.co", "Lily9@m.co"],
                ["Lily", "Lily15@m.co", "Lily16@m.co"],
                ["Lily", "Lily19@m.co", "Lily20@m.co"],
                ["Lily", "Lily6@m.co", "Lily7@m.co"],
                ["Lily", "Lily10@m.co", "Lily11@m.co"],
                ["Lily", "Lily5@m.co", "Lily6@m.co"],
                ["Lily", "Lily13@m.co", "Lily14@m.co"],
                ["Lily", "Lily9@m.co", "Lily10@m.co"],
                ["Lily", "Lily1@m.co", "Lily2@m.co"],
                ["Lily", "Lily3@m.co", "Lily4@m.co"],
                ["Lily", "Lily2@m.co", "Lily3@m.co"],
                ["Lily", "Lily11@m.co", "Lily12@m.co"],
                ["Lily", "Lily7@m.co", "Lily8@m.co"],
                ["Lily", "Lily12@m.co", "Lily13@m.co"],
                ["Lily", "Lily18@m.co", "Lily19@m.co"],
                ["Lily", "Lily17@m.co", "Lily18@m.co"],
                ["Lily", "Lily16@m.co", "Lily17@m.co"],
                ["Lily", "Lily14@m.co", "Lily15@m.co"],
                ["Lily", "Lily0@m.co", "Lily1@m.co"],
            ],
            [
                [
                    [
                        "Lily",
                        "Lily0@m.co",
                        "Lily10@m.co",
                        "Lily11@m.co",
                        "Lily12@m.co",
                        "Lily13@m.co",
                        "Lily14@m.co",
                        "Lily15@m.co",
                        "Lily16@m.co",
                        "Lily17@m.co",
                        "Lily18@m.co",
                        "Lily19@m.co",
                        "Lily1@m.co",
                        "Lily20@m.co",
                        "Lily2@m.co",
                        "Lily3@m.co",
                        "Lily4@m.co",
                        "Lily5@m.co",
                        "Lily6@m.co",
                        "Lily7@m.co",
                        "Lily8@m.co",
                        "Lily9@m.co",
                    ],
                ]
            ],
        ),
    ],
)
def test_accounts_merge(accounts: list[list[str]], expected: list[list[str]]) -> None:
    result = accounts_merge(accounts)
    assert _emails_are_sorted(result), "각 계정의 이메일이 정렬되어 있어야 합니다"
    assert _sort_by_account(result) == _sort_by_account(expected)
