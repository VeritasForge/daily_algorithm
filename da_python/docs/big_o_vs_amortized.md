# Big O vs Amortized Analysis

## 개요

알고리즘의 시간 복잡도를 분석하는 두 가지 방법을 비교합니다.

| 분석 방법 | 관점 | 질문 |
|-----------|------|------|
| **Big O (Worst Case)** | 단일 연산 | "이 연산이 최악의 경우 얼마나 걸릴까?" |
| **Amortized** | 연산 시퀀스 | "여러 연산의 평균 비용은 얼마일까?" |

---

## Big O (Worst Case Analysis)

### 정의

단일 연산의 **최악의 경우** 시간 복잡도를 분석합니다.

### 특징

- 모든 연산에 대해 **보장된 상한선** 제공
- 가장 보수적인 추정치
- 상수 계수 무시: O(3n) = O(n), O(1.5) = O(1)

### 예제: Python 리스트

```python
arr = [1, 2, 3, 4, 5]

arr[2]          # O(1) - 인덱스 접근
arr.append(6)   # O(1) - 끝에 추가 (대부분의 경우)
arr.insert(0, 0) # O(n) - 맨 앞 삽입 (모든 요소 이동)
```

### 한계

Big O만으로는 **가끔 비싼 연산**이 포함된 자료구조를 정확히 평가하기 어렵습니다.

```python
# Dynamic Array (Python list)의 append
arr = []
for i in range(n):
    arr.append(i)  # 대부분 O(1), 가끔 O(n)
```

- 공간이 부족하면 **배열 재할당** 발생 → O(n)
- Big O 관점: append는 O(n) (최악의 경우)
- 하지만 실제로는 거의 O(1)처럼 동작

---

## Amortized Analysis (분할 상환 분석)

### 정의

**연속된 연산들의 총 비용**을 연산 횟수로 나눈 **평균 비용**을 분석합니다.

### 핵심 아이디어

> 비싼 연산이 가끔 발생하더라도, 그 비용을 여러 연산에 "분할 상환"하면
> 연산당 평균 비용이 낮아질 수 있다.

### 예제 1: Dynamic Array의 append

```
초기 용량: 4

append(1): [1, _, _, _]       O(1)
append(2): [1, 2, _, _]       O(1)
append(3): [1, 2, 3, _]       O(1)
append(4): [1, 2, 3, 4]       O(1)
append(5): 용량 부족! 재할당 필요
           [1, 2, 3, 4, _, _, _, _]  ← 새 배열 (용량 8)
           4개 요소 복사 → O(n)
```

**비용 분석 (n개 요소 추가 시):**

| 항목 | 비용 |
|------|------|
| 일반 append | n회 × O(1) = O(n) |
| 재할당 (1+2+4+8+...+n) | O(n) |
| **총 비용** | **O(2n)** |
| **연산당 평균** | O(2n) / n = **O(1)** |

### 예제 2: 스택 2개로 구현한 큐

```python
class MyQueue:
    def __init__(self):
        self.stack_in = []   # push용
        self.stack_out = []  # pop용

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if not self.stack_out:
            # stack_in의 모든 요소를 stack_out으로 이동
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
```

**동작 예시:**

```
push(1), push(2), push(3):
  stack_in:  [1, 2, 3]
  stack_out: []

pop():  ← transfer 발생!
  stack_in:  []
  stack_out: [3, 2, 1]
  반환: 1

pop():  ← transfer 없음 (stack_out에 요소 있음)
  stack_out: [3, 2]
  반환: 2
```

**비용 분석:**

```
각 요소의 여정:
  push    transfer    pop
   ↓         ↓         ↓
  [IN] ──→ [OUT] ──→ 반환
   1회      1회       1회
```

- 각 요소는 **최대 3번**의 기본 연산을 거침
- n개 요소 처리 시 총 비용: O(3n)
- 총 연산 횟수: 2n (push n회 + pop n회)
- **연산당 평균: O(3n) / 2n = O(1.5) = O(1)**

---

## 비교 요약

### 분석 관점

```
Big O (Worst Case):
┌─────────────────────────────────┐
│ 연산1  연산2  연산3  ... 연산n      |
│   ↓                             │
│ "가장 비싼 놈이 얼마야?"             |
└─────────────────────────────────┘

Amortized:
┌─────────────────────────────────┐
│ 연산1  연산2  연산3  ...  연산n     |
│   └──────┴──────┴─────────┘     │
│        "전체 평균이 얼마야?"        |
└─────────────────────────────────┘
```

### 실제 사례 비교

| 자료구조/연산 | Big O (Worst) | Amortized |
|---------------|---------------|-----------|
| Dynamic Array append | O(n) | O(1) |
| Hash Table insert | O(n) | O(1) |
| Splay Tree search | O(n) | O(log n) |
| Stack Queue pop | O(n) | O(1) |

### 언제 어떤 분석을 사용할까?

| 상황 | 권장 분석 |
|------|-----------|
| 실시간 시스템 (지연 허용 불가) | Big O |
| 일반적인 성능 평가 | Amortized |
| 단일 연산 보장이 필요할 때 | Big O |
| 전체 처리량이 중요할 때 | Amortized |

---

## 비유로 이해하기

### 월급과 연봉

```
Big O = 월급의 최저치
  → "최악의 달에도 최소 이만큼은 받아"

Amortized = 월 평균 소득
  → "보너스 달도 있고 적은 달도 있지만, 평균 내면 이 정도야"
```

### 출퇴근 시간

```
Big O = 최악의 출퇴근 시간
  → "사고 나면 2시간 걸릴 수도 있어"

Amortized = 평균 출퇴근 시간
  → "보통은 30분, 가끔 오래 걸려도 평균 내면 35분이야"
```

---

## 참고

- Big O에서 상수 계수는 무시: O(1) = O(2) = O(100)
- Amortized O(1)이라도 **개별 연산은 O(n)** 일 수 있음
- Amortized 분석은 **확률이 아닌 확정적 분석** (Average Case와 다름)
