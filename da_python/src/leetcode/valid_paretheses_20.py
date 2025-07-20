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

closed_parethese = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def is_valid(s: str) -> bool:
    stack: list[str] = []
    for c in s:
        if not stack or c in closed_parethese:
            stack.append(closed_parethese[c])
        else:
            if c == stack[-1]:
                stack.pop()
            else:
                return False

    return not stack
