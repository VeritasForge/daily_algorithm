"""
1309. Decrypt String from Alphabet to Integer Mapping
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

Difficulty: Easy

문제 설명:
    숫자와 '#'으로 구성된 문자열 s가 주어진다.
    s를 영어 소문자로 매핑하려 한다:

    - 'a' ~ 'i'는 '1' ~ '9'로 표현된다.
    - 'j' ~ 'z'는 '10#' ~ '26#'로 표현된다.

    매핑 후 형성된 문자열을 반환하라.
    테스트 케이스는 항상 유일한 매핑이 존재하도록 생성된다.

제약 조건:
    - 1 <= s.length <= 1000
    - s는 숫자와 '#' 문자로만 구성
    - s는 항상 유효한 매핑이 가능한 문자열
"""


def freq_alphabets(s: str) -> str:
    raise NotImplementedError
