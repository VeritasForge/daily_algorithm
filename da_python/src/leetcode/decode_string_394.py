# https://leetcode.com/problems/decode-string/
# 394. Decode String
#
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
#
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
#
# Constraints:
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].


def decode_string(s: str) -> str:
    stack: list[tuple[int, list[str]]] = []
    open_stack: list[bool] = []
    is_nested: bool = False
    res: str = ""

    for c in s:
        if c == "[":
            open_stack.append(True)
            is_nested = len(open_stack) > 1
        elif c == "]":  # close
            num, chars = stack.pop()
            open_stack.pop()

            if is_nested:
                res = num * ("".join(chars) + res)
            else:
                res += num * "".join(chars)

            if len(open_stack) == 0:
                is_nested = False
        elif not open_stack:
            if c.isdigit():
                stack.append((int(c), []))
            else:
                res += c
        elif open_stack[-1]:
            if c.isdigit():
                stack.append((int(c), []))
            else:
                stack[-1][1].append(c)
        else:
            raise ValueError(f"Unexpected Value: {c}")

    return res