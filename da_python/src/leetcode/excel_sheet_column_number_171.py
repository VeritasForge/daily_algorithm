"""
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/

Difficulty: Easy

문제 설명:
    Given a string columnTitle that represents the column title as appears in an
    Excel sheet, return its corresponding column number.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

    Example 1:

    Input: columnTitle = "A"
    Output: 1

    Example 2:

    Input: columnTitle = "AB"
    Output: 28

    Example 3:

    Input: columnTitle = "ZY"
    Output: 701

제약 조건:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].
"""


def title_to_number(column_title: str) -> int:
    num = 0
    for c in column_title:
        num = num * 26 + (ord(c) - ord("A") + 1)
    return num

# def title_to_number(column_title: str) -> int:
#     num = 0
#     for i, c in enumerate(reversed(column_title)):
#         num += 26 ** i * (ord(c) - ord("A") + 1)
#     return num
