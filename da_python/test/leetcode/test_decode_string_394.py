import pytest
from src.leetcode.decode_string_394 import decode_string


@pytest.mark.parametrize(
    "s, expected",
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("2[a2[c]]3[cd]ef", "accacccdcdcdef"),
        ("10[a]", "aaaaaaaaaa"),
        ("12[ab]", "abababababababababababab"),
        ("3[a10[b]]", "abbbbbbbbbbabbbbbbbbbbabbbbbbbbbb"),
        (
            "3[z]2[2[y]pq4[2[jk]e1[f]]]ef",
            "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef",
        ),
    ],
)
def test_decode_string(s: str, expected: str):
    assert decode_string(s) == expected
