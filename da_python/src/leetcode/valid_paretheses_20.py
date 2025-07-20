"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

parentheses_map = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def is_valid(s: str) -> bool:
    stack: list[str | None] = []
    for c in s:
        if not stack or c in parentheses_map:
            stack.append(parentheses_map.get(c))
        elif c != stack.pop():
            return False

    return not stack
