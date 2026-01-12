import pytest

from src.leetcode.string_to_integer_atoi_8 import my_atoi


@pytest.mark.parametrize(
    "s, expected",
    [
        # Example 1: Basic positive number
        ("42", 42),
        # Example 2: Leading whitespace and negative sign
        ("   -42", -42),
        # Example 3: Reading stops at non-digit character
        ("1337c0d3", 1337),
        # Example 4: Overflow - clamp to INT_MIN
        ("-91283472332", -2147483648),
        # Example 5: Non-digit after initial digit
        ("0-1", 0),
        # Additional edge cases
        # Leading whitespace with positive sign
        ("   +42", 42),
        # Only whitespace
        ("   ", 0),
        # Empty string
        ("", 0),
        # Starts with non-digit
        ("words and 987", 0),
        # Overflow - clamp to INT_MAX
        ("91283472332", 2147483647),
        # Leading zeros
        ("0000000000012345678", 12345678),
        # INT_MIN boundary
        ("-2147483648", -2147483648),
        # INT_MAX boundary
        ("2147483647", 2147483647),
        # Just below overflow
        ("-2147483647", -2147483647),
        # ========== 추가 엣지케이스 ==========
        # 부호만 있는 경우
        ("+", 0),
        ("-", 0),
        ("   +", 0),
        ("   -", 0),
        # 부호 뒤 비숫자
        ("+abc", 0),
        ("-abc", 0),
        ("+.", 0),
        # 소수점 처리 (정수 부분만 읽음)
        ("3.14159", 3),
        ("-3.14", -3),
        (".5", 0),  # 숫자로 시작하지 않음
        # 숫자 사이 공백 (첫 숫자만 읽음)
        ("4 2", 4),
        ("  123 456", 123),
        # 여러 부호
        ("+-12", 0),
        ("--12", 0),
        ("++12", 0),
        ("-+12", 0),
        # 0 처리
        ("0", 0),
        ("000", 0),
        ("-0", 0),
        ("+0", 0),
        ("  -0012a42", -12),
        # 부호와 공백 사이
        ("+ 42", 0),  # 부호 바로 뒤가 숫자가 아님
        ("- 42", 0),
        # 특수문자로 시작
        (".42", 0),
        # (",42", 0),
        # 탭/개행 (선행 공백만 무시)
        # ("\t42", 0),  # 탭은 strip 대상 아님 (문제 정의상 공백만)
        # ("\n42", 0),
        # 매우 긴 숫자 (오버플로우 테스트)
        ("9999999999999999999999999999", 2147483647),
        ("-9999999999999999999999999999", -2147483648),
        # 경계값 +-1
        ("2147483646", 2147483646),
        ("2147483648", 2147483647),  # INT_MAX + 1 → 클램핑
        ("-2147483649", -2147483648),  # INT_MIN - 1 → 클램핑
        ("-91283472332", -2147483648),
    ],
)
def test_my_atoi(s: str, expected: int) -> None:
    assert my_atoi(s) == expected
