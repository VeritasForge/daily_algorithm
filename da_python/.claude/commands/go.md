---
description: LeetCode 문제 스캐폴딩 (소스 + 테스트 파일 생성)
argument-hint: <leetcode-url>
---

# LeetCode 문제 스캐폴딩

LeetCode URL: $1

## 작업 순서

1. **URL에서 문제 정보 추출**
   - 문제 번호
   - 문제 제목 (snake_case로 변환)

2. **LeetCode 페이지에서 정보 수집**
   - 문제 설명
   - 함수 시그니처
   - 예제 입출력

3. **소스 파일 생성**: `src/leetcode/{문제명}_{번호}.py`
   - 상단 주석: URL, 제목, 난이도, 문제 설명
   - 일반 함수로 작성 (클래스 메서드 X)
   - 함수 시그니처만 작성, 구현부는 `raise NotImplementedError`
   - Type hint: Python 3.9+ 스타일 (`list[int]`, `TreeNode | None`)
   - 자료구조 필요시 `src/common`에서 import

4. **테스트 파일 생성**: `test/leetcode/test_{문제명}_{번호}.py`
   - pytest + parametrize 사용
   - LeetCode 예제를 테스트 케이스로 포함
   - 자료구조 필요시 헬퍼 함수 import (`create_linked_list`, `list_to_tree` 등)

## 파일명 규칙

- snake_case 사용
- 형식: `{문제_제목}_{문제_번호}.py`
- 예: `two_sum_1.py`, `add_two_numbers_2.py`

## 자료구조 import 규칙

필요한 경우에만 `src/common`에서 import:
- LinkedList: `from src.common.linked_list import ListNode, create_linked_list, create_list`
- Tree: `from src.common.tree import TreeNode, list_to_tree, find_node`

---

위 URL의 LeetCode 문제에 대해 소스 파일과 테스트 파일을 생성해주세요.
