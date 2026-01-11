"""
LeetCode 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

난이도: Medium

문제:
주어진 문자열 s에서 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하라.
부분 문자열(substring)은 문자열 내에서 연속된 문자들의 시퀀스이다.

제약조건:
- 0 <= s.length <= 5 * 10^4
- s는 영문자, 숫자, 기호, 공백으로 구성됨
"""


def length_of_longest_substring(s: str) -> int:
    """
    중복 문자가 없는 가장 긴 부분 문자열의 길이를 반환한다.

    Args:
        s: 입력 문자열

    Returns:
        중복 없는 가장 긴 부분 문자열의 길이
    """
    char_idx = {}
    max_len = left = 0

    for right, c in enumerate(s):
        if c in char_idx and left <= char_idx[c]:
            left = char_idx[c] + 1

        char_idx[c] = right
        max_len = max(max_len, right - left + 1)

    return max_len
