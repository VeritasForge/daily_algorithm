"""
721. Accounts Merge
https://leetcode.com/problems/accounts-merge/

Difficulty: Medium

문제 설명:
    accounts 리스트가 주어진다. 각 accounts[i]는 문자열 리스트로,
    첫 번째 원소 accounts[i][0]은 이름이고, 나머지 원소들은 해당 계정의
    이메일 주소들이다.

    같은 이메일을 공유하는 두 계정은 반드시 같은 사람의 계정이다.
    같은 이름을 가진 계정이라도 다른 사람일 수 있다.

    계정을 병합한 후, 각 계정의 첫 번째 원소는 이름이고
    나머지 이메일은 정렬된 순서로 반환한다.
    계정 자체의 순서는 상관없다.

제약 조건:
    - 1 <= accounts.length <= 1000
    - 2 <= accounts[i].length <= 10
    - 1 <= accounts[i][j].length <= 30
    - accounts[i][0]은 영문자로 구성
    - accounts[i][j] (j > 0)은 유효한 이메일
"""

import ipdb


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    offset: int = 0
    res: list[list[str]] = []
    while len(accounts) > offset:
        for _, acc_i in enumerate(accounts, start=offset):
            for _, acc_j in enumerate(accounts[offset + 1 :], start=offset + 1):
                if acc_i[0] == acc_j[0]:
                    set_i, set_j = set(acc_i[1:]), set(acc_j[1:])
                    if not set_i.isdisjoint(set_j):
                        acc_i = [acc_i[0]] + list(set_i | set_j)

            if all(set(acc[1:]).isdisjoint(acc_i[1:]) for acc in res):
                ipdb.set_trace()
                res.append([acc_i[0]] + list(set(acc_i[1:])))
            else:
                ipdb.set_trace()
                find_i, result = -1, set()
                for i, item in enumerate(res):
                    if item[0] == acc_i[0]:
                        result = set(item[1:]) | (set(acc_i[1:]) - set(item[1:]))
                        find_i = i
                        break

                del res[find_i]
                res.append([acc_i[0]] + list(result))

            offset += 1

    return [[item[0]] + sorted(item[1:]) for item in res]

    # offset: int = 0
    # res: list[list[str]] = []
    # while len(accounts) > offset:
    #     for _, acc_i in enumerate(accounts, start=offset):
    #         for _, acc_j in enumerate(accounts[offset + 1 :], start=offset + 1):
    #             if acc_i[0] == acc_j[0]:
    #                 set_i, set_j = set(acc_i[1:]), set(acc_j[1:])
    #                 if not set_i.isdisjoint(set_j):
    #                     acc_i = [acc_i[0]] + list(set_i | set_j)
    #
    #         if all(set(acc[1:]).isdisjoint(acc_i[1:]) for acc in res):
    #             res.append(acc_i)
    #         offset += 1
    #
    # return [[item[0]] + sorted(item[1:]) for item in res]
