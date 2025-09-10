"""
URL: https://leetcode.com/problems/climbing-stairs/
Title: 70. Climbing Stairs
---
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

"""
  계단 오르기 문제(Climbing Stairs) 완벽 이해하기

  1. 문제 정의

  '계단 오르기' 문제는 컴퓨터 과학과 수학에서 매우 유명한 입문 문제입니다. 문제는 보통 다음과 같이 주어집니다.

  > "총 n개의 계단이 있습니다. 당신은 한 번에 1계단 또는 2계단씩 오를 수 있습니다. 이 때, 계단 꼭대기까지 오르는
  방법은 총 몇 가지일까요?"

  이 문제는 겉보기엔 간단하지만, 그 안에는 중요한 수학적 원리와 효율적인 문제 해결 기법이 숨어있습니다.

  ---

  2. 가장 쉽게 이해하는 방법: '마지막 한 걸음'의 비밀

  이 문제의 핵심은 "목표 지점에 도착하기 직전, 마지막 한 걸음은 어디서 내디뎠을까?"를 생각하는 것입니다.

  귀여운 토끼가 계단을 오른다고 상상해봅시다. 토끼는 1칸(폴짝!) 또는 2칸(폴~짝!)만 뛸 수 있습니다.

   * 1층 가는 법: 폴짝! (1가지)
   * 2층 가는 법: 폴짝! 폴짝! 또는 폴~짝! (2가지)

  ▶ 3층으로 가는 법

  3층에 도착하려면, 토끼의 마지막 점프는 반드시 아래 둘 중 하나여야 합니다.
   1. 2층에 있다가 → 1칸을 뛰어 3층에 도착
   2. 1층에 있다가 → 2칸을 뛰어 3층에 도착

  따라서 3층으로 가는 모든 방법의 수는, 단순히 두 경우의 수를 더하면 됩니다.
  > (2층까지 가는 방법의 수) + (1층까지 가는 방법의 수) = 2 + 1 = 3가지

  ▶ 가장 많이 하는 질문: "어? 1층에서 바로 4층으로 갈 수는 없나요?"

  아주 좋은 질문입니다! 4층으로 가는 방법을 생각할 때, 왜 3층과 2층만 고려하고 1층은 생각하지 않을까요?

  그 이유는 '마지막 한 걸음'의 규칙 때문입니다. 1층에서는 4층으로 한 번에 3칸을 뛰어야 하므로 규칙에 맞지 않습니다.

  "하지만 1층 → 2층 → 4층 처럼 1층을 거쳐가는 길도 있잖아요?"

  맞습니다. 그리고 그 길은 우리가 '2층까지 가는 방법'을 셀 때 이미 그 안에 포함되어 있습니다.

  레고 블록을 쌓는다고 생각해보세요. 4층짜리 성을 만들려면,
   * 이미 완성된 3층 성 위에 1층 블록을 얹거나,
   * 이미 완성된 2층 성 위에 2층 블록을 얹어야 합니다.

  '3층 성을 만드는 방법' 안에는 이미 '1층을 거쳐 만드는 방법'이 모두 들어있습니다. 따라서 우리는 그냥 완성된 3층과
  2층의 경우의 수만 더하면, 모든 경로를 빠짐없이 계산하게 되는 것입니다.

  ---

  3. 수학적 원리: 피보나치 수열 (Fibonacci Sequence)

  위에서 발견한 규칙을 일반화하면 다음과 같은 공식을 얻을 수 있습니다.

  > `ways(n) = ways(n-1) + ways(n-2)`

  n번째 계단에 오르는 방법의 수는 n-1번째 계단에 오르는 방법의 수와 n-2번째 계단에 오르는 방법의 수의 합과 같습니다.

  이는 피보나치 수열의 정의와 정확히 일치합니다.
   * ways(1) = 1
   * ways(2) = 2
   * ways(3) = 2 + 1 = 3
   * ways(4) = 3 + 2 = 5
   * ways(5) = 5 + 3 = 8
   * ...


"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev, curr = 1, 2
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    return curr
