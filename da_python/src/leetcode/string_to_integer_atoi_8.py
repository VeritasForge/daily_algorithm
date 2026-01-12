# https://leetcode.com/problems/string-to-integer-atoi
# 8. String to Integer (atoi)
# Difficulty: Medium
#
# Implement the myAtoi(string s) function, which converts a string to a
# 32-bit signed integer.
#
# The algorithm for myAtoi(string s) is as follows:
#
# 1. Whitespace: Ignore any leading whitespace (" ").
#
# 2. Signedness: Determine the sign by checking if the next character is
#    '-' or '+', assuming positivity if neither present.
#
# 3. Conversion: Read the integer by skipping leading zeros until a non-digit
#    character is encountered or the end of the string is reached.
#    If no digits were read, then the result is 0.
#
# 4. Rounding: If the integer is out of the 32-bit signed integer range
#    [-2^31, 2^31 - 1], then round the integer to remain in the range.
#    Specifically, integers less than -2^31 should be rounded to -2^31,
#    and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
#
# 5. Return the integer as the final result.
#
# Constraints:
# - 0 <= s.length <= 200
# - s consists of English letters (lower-case and upper-case), digits (0-9),
#   ' ', '+', '-', and '.'.

import string

INT_MIN = -(2**31)  # -2147483648
INT_MAX = 2**31 - 1  # 2147483647
STOP_CHARS = set(string.ascii_letters + "+-. ")


def my_atoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0

    sign, idx = 1, 0
    if s[0] in "+-":
        sign = 1 if s[0] == "+" else -1
        idx += 1

    num = 0
    while idx < len(s) and s[idx].isdigit():
        num = num * 10 + int(s[idx])
        idx += 1

        if sign * num <= INT_MIN:
            return INT_MIN
        if sign * num >= INT_MAX:
            return INT_MAX

    return num * sign
