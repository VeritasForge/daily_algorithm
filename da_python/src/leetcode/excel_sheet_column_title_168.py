"""
168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"

Constraints:

1 <= columnNumber <= 2^31 - 1
"""


def convert_to_title(column_number: int) -> str:
    """0이 없는 26진법(base-26) 변환.

    일반적인 진법 변환(예: 10진수 -> 2진수)과 같은 원리로
    나머지(% 26)로 현재 자리 문자를, 몫(// 26)으로 다음 자리로 넘길 값을 구한다.
    다른 점은 A~Z가 1~26에 대응되어 "0"에 해당하는 문자가 없다는 것뿐이다.

    왜 매 반복마다 `column_number -= 1`을 먼저 하는가:
        알파벳은 1-indexed(A=1)인데 나머지 연산은 0-indexed 결과(0~25)를 준다.
        26의 배수(26, 52, 702...)에서 보정 없이 나누면 `26 % 26 == 0`이 되어
        Z(26번째)가 아닌 A(0번째)로 잘못 매핑된다.
        예: n=26 -> -1 보정 없이 그대로 나누면 26 % 26 = 0 -> 'A' (오답).
            -1 보정 후 25 % 26 = 25 -> 'Z' (정답).

    왜 26으로 나누는가 (그룹 개념):
        알파벳 26개를 한 묶음(1자리)으로 보고, 26개를 다 쓰면 새로운 자리가 생긴다.
        `// 26`은 "지금까지 몇 개의 26-묶음을 다 채웠는지"를 구하는 연산이고,
        이 몫이 다음 반복에서 "그 다음 자리 문자"를 결정하는 데 재사용된다.
        예: 701 -1=700 -> 700 % 26 = 24('Y'), 700 // 26 = 26
                          26 -1=25 -> 25 % 26 = 25('Z'), 25 // 26 = 0 (종료)
            => 자릿수 개수(26, 676, 17576...)는 상자 개수의 크기가 아니라
               나눗셈을 몇 번 반복해야 몫이 0이 되는지로 결정된다.

    왜 마지막에 뒤집는가:
        나눗셈은 항상 끝자리(1의 자리)부터 값을 알려주고 첫자리는 가장 나중에 나온다.
        10진수 1234를 %10, //10으로 뽑으면 [4,3,2,1] 순서로 나오는 것과 동일한 이유로,
        계산 순서(끝자리->첫자리)와 표기 순서(첫자리->끝자리)가 반대라 뒤집어야 한다.

    2진법 변환과의 비교:
        13 -> 2진수 변환(% 2, // 2)도 뼈대는 완전히 동일하다(나머지로 자리 확정,
        몫을 다음 반복에 넘기고, 끝에서 뒤집기). 유일한 차이는 2진법은 0이 정상적인
        숫자라 `-1` 보정이 필요 없다는 점 -- 이 문제만 A=1(0 없음)이라 보정이 필요하다.

    Args:
        column_number: 1 이상 2^31 - 1 이하의 정수.

    Returns:
        1-indexed 26진법으로 표현한 엑셀 열 제목 문자열.

    Time: O(log_26 n) -- 매 반복마다 26으로 나누므로 반복 횟수는 log_26(n)에 비례.
    Space: O(log_26 n) -- 결과 문자열 길이(최대 7자, n=2^31-1 기준)만큼의 리스트.
    """
    letters = []
    while column_number > 0:
        column_number -= 1
        letters.append(chr(ord("A") + column_number % 26))
        column_number //= 26

    return "".join(reversed(letters))
