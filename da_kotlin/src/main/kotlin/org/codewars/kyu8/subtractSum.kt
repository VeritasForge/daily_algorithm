// https://www.codewars.com/kata/56c5847f27be2c3db20009c3/train/kotlin
//
// 8 kyu
// Never visit a . . . !?
//
// Complete the function which get an integer n (n > 0) and return "apple"
//
// NOTE: The fruit list is not necessary to solve this problem.
//
// The number n is given (10 < n < 10000), you have to do the following procedure until n becomes smaller than or equal to 100:
// - subtract from n the sum of its digits
// - if the new n is in the list of fruits, return the corresponding fruit
//
// n = 325
// sum of digits = 3 + 2 + 5 = 10
// n = 325 - 10 = 315
// ...
//
// 1-kiwi
// 2-pear
// 3-kiwi
// 4-banana
// 5-melon
// 6-banana
// 7-melon
// 8-pineapple
// 9-apple
// 10-pineapple
// ...
// 99-apple
// 100-apple
//
// As you can see, the result is always "apple".

package org.codewars.kyu8

val fruitMap = mapOf(
    1 to "kiwi",
    2 to "pear",
    3 to "kiwi",
    4 to "banana",
    5 to "melon",
    6 to "banana",
    7 to "melon",
    8 to "pineapple",
    9 to "apple",
    10 to "pineapple",
    11 to "cucumber",
    12 to "pineapple",
    13 to "cucumber",
    14 to "orange",
    15 to "grape",
    16 to "orange",
    17 to "grape",
    18 to "apple",
    19 to "grape",
    20 to "cherry",
    21 to "pear",
    22 to "cherry",
    23 to "pear",
    24 to "kiwi",
    25 to "banana",
    26 to "kiwi",
    27 to "apple",
    28 to "melon",
    29 to "banana",
    30 to "melon",
    31 to "pineapple",
    32 to "melon",
    33 to "pineapple",
    34 to "cucumber",
    35 to "orange",
    36 to "apple",
    37 to "orange",
    38 to "grape",
    39 to "orange",
    40 to "grape",
    41 to "cherry",
    42 to "pear",
    43 to "cherry",
    44 to "pear",
    45 to "apple",
    46 to "pear",
    47 to "kiwi",
    48 to "banana",
    49 to "kiwi",
    50 to "banana",
    51 to "melon",
    52 to "pineapple",
    53 to "melon",
    54 to "apple",
    55 to "cucumber",
    56 to "pineapple",
    57 to "cucumber",
    58 to "orange",
    59 to "cucumber",
    60 to "orange",
    61 to "grape",
    62 to "cherry",
    63 to "apple",
    64 to "cherry",
    65 to "pear",
    66 to "cherry",
    67 to "pear",
    68 to "kiwi",
    69 to "pear",
    70 to "kiwi",
    71 to "banana",
    72 to "apple",
    73 to "banana",
    74 to "melon",
    75 to "pineapple",
    76 to "melon",
    77 to "pineapple",
    78 to "cucumber",
    79 to "pineapple",
    80 to "cucumber",
    81 to "apple",
    82 to "grape",
    83 to "orange",
    84 to "grape",
    85 to "cherry",
    86 to "grape",
    87 to "cherry",
    88 to "pear",
    89 to "cherry",
    90 to "apple",
    91 to "kiwi",
    92 to "banana",
    93 to "kiwi",
    94 to "banana",
    95 to "melon",
    96 to "banana",
    97 to "melon",
    98 to "pineapple",
    99 to "apple",
    100 to "pineapple"
)

//fun subtractSum(n: Int): String {
//    var num = n
//    do {
//        num -= num.toString().sumOf { it.digitToInt() }
//    } while (num !in fruitMap)
//
//    return fruitMap.getValue(num)
//}


//fun subtractSum(n: Int): String {
//    val key = n - n.toString().sumOf { it.digitToInt() }
//    if (key in fruitMap) return fruitMap.getValue(key)
//    return subtractSum(key)
//}

/*
문자의 숫자 표현 (ASCII/Unicode)

  컴퓨터 내부에서 모든 문자(Character)는 사실 숫자로
  저장됩니다. 이 규칙을 정의한 것이 ASCII(아스키)나
  Unicode(유니코드) 같은 문자 인코딩 표준입니다.

  중요한 점은, 숫자 '0'부터 '9'까지의 문자들은 연속된 숫자
  코드로 할당되어 있다는 것입니다.

   * 문자 '0'은 숫자 48
   * 문자 '1'은 숫자 49
   * 문자 '2'은 숫자 50
   * ...
   * 문자 '9'은 숫자 57

  '0'을 빼는 원리

  Kotlin에서 Char 타입에 산술 연산(-)을 사용하면, 이
  문자들은 내부적으로 자신의 숫자 코드(정수)로 변환되어
  계산됩니다.

  따라서 it - '0' 코드는 다음과 같이 동작합니다.

   * it이 문자 '3'이라면:
       * '3' - '0'
       * 내부적으로는 51 - 48 이 실행됩니다.
       * 결과는 정수 3이 됩니다.

   * it이 문자 '8'이라면:
       * '8' - '0'
       * 내부적으로는 56 - 48 이 실행됩니다.
       * 결과는 정수 8이 됩니다.

  결론적으로, 어떤 숫자 문자에서 '0' 문자의 숫자 코드를
  빼면, 해당 문자가 나타내는 실제 정수 값을 얻을 수
  있습니다.

  ---

  it.digitToInt() 와의 비교

  이전에 제가 설명해 드린 it.digitToInt()와 it - '0'는 사실상
   거의 같은 결과를 반환합니다. 하지만 중요한 차이점이
  있습니다.

   * `it.digitToInt()`
       * 가독성: digitToInt(숫자로 변환)라는 이름에서 의도가
         명확하게 드러납니다.
       * 안전성: 해당 문자가 (10진수) 숫자가 아니면
         IllegalArgumentException을 발생시켜 에러를
         알려줍니다.
       * 언어 스타일: Kotlin의 표준 라이브러리 함수를 사용하는
         관용적인(Idiomatic) 방식입니다.
       * 성능: 함수 호출 및 에러 체크로 인해 이론적으로는 아주
         약간의 오버헤드가 있을 수 있습니다.

   * `it - '0'`
       * 가독성: 원리를 모르면 이해하기 어렵습니다.
       * 안전성: 문자가 숫자가 아니어도 일단 계산은 됩니다.
         (예: 'a' - '0' = 97 - 48 = 49) 의도치 않은 결과를
         낳을 수 있습니다.
       * 언어 스타일: C나 Java의 저수준(low-level) 스타일에
         가깝습니다.
       * 성능: 직접 연산하므로 매우 빠릅니다. 하지만 대부분의
         경우 성능 차이는 무시할 수 있는 수준입니다.

  결론:
  특별히 극단적인 성능 최적화가 필요한 상황이 아니라면,
  코드의 명확성과 안전성을 위해 `it.digitToInt()`를 사용하는
  것이 훨씬 좋은 선택입니다.

  ---

  Python 및 Golang과의 비교

   * Python:
      Python에서는 이런 연산이 불가능합니다. '3' - '0'
  코드는 TypeError를 발생시킵니다. Python에서는 int('3')
  처럼 명시적인 형변환 함수를 사용해야 합니다.

   1     # TypeError: unsupported operand type(s)
     for -: 'str' and 'str'
   2     # error = '3' - '0'
   3
   4     # 올바른 방법
   5     digit = int('3')

   * Golang:
      Go는 C와 유사하게 rune 타입(문자)이 사실상
  정수(int32)의 별칭(alias)이므로 이 방식이 잘 동작합니다.

   1     digit := int('3' - '0') // 결과는 정수 3
   2     fmt.Println(digit)

 */
fun subtractSum(n: Int): String {
    val key = n - n.toString().sumOf { it - '0' }
    if (key in fruitMap) return fruitMap.getValue(key)
    return subtractSum(key)
}
