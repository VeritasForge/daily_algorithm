"""
383. Ransom Note
https://leetcode.com/problems/ransom-note

Difficulty: Easy

Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
    - 1 <= ransomNote.length, magazine.length <= 10^5
    - ransomNote and magazine consist of lowercase English letters.
"""

from collections import Counter


# def can_construct(ransom_note: str, magazine: str) -> bool:
#     counter_ransom_note = Counter(ransom_note)
#     counter_magazine = Counter(magazine)
#
#     for k, v in counter_ransom_note.items():
#         if k not in counter_magazine:
#             return False
#
#         if v > counter_magazine[k]:
#             return False
#
#     return True


def can_construct(ransom_note: str, magazine: str) -> bool:
    counter_magazine = Counter(magazine)
    return all(counter_magazine.get(k, 0) >= v for k, v in Counter(ransom_note).items())


# def can_construct(ransom_note: str, magazine: str) -> bool:
#     return not (Counter(ransom_note) - Counter(magazine))
