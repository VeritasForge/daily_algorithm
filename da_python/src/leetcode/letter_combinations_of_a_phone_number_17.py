"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

17. Letter Combinations of a Phone Number (Medium)

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

    2 -> abc
    3 -> def
    4 -> ghi
    5 -> jkl
    6 -> mno
    7 -> pqrs
    8 -> tuv
    9 -> wxyz

Constraints:
    - 0 <= digits.length <= 4
    - digits[i] is a digit in the range ['2', '9']
"""

num_str = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    res = []

    def f(idx, current):
        if idx >= len(digits):
            res.append(current)
            return

        for i, c in enumerate(num_str[digits[idx]]):
            f(idx + 1, current + c)

    f(0, "")
    return res
