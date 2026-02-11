---
description: LeetCode 문제 스캐폴딩 (소스 + 테스트 파일 생성)
argument-hint: <leetcode-url>
allowed-tools: Bash, Read, Write, Glob
---

# LeetCode 문제 스캐폴딩

LeetCode URL: $ARGUMENTS

## 작업 순서

### Step 1: URL에서 titleSlug 추출

URL에서 `titleSlug`를 추출합니다.
- `https://leetcode.com/problems/two-sum/` → `two-sum`
- `https://leetcode.com/problems/two-sum/description/` → `two-sum`

### Step 2: GraphQL API로 문제 정보 수집

다음 bash 명령어로 문제 정보를 가져옵니다:

```bash
curl -s -X POST "https://leetcode.com/graphql" \
  -H "Content-Type: application/json" \
  -d '{"query":"query { question(titleSlug: \"<titleSlug>\") { questionId title titleSlug difficulty content codeSnippets { lang langSlug code } }}"}'
```

응답에서 추출할 정보:
- `questionId`: 문제 번호
- `title`: 문제 제목
- `difficulty`: 난이도 (Easy/Medium/Hard)
- `content`: 문제 설명 (HTML → 텍스트로 변환)
- `codeSnippets`: `langSlug == "python3"`인 항목에서 함수 시그니처 추출

### Step 3: 함수 시그니처 변환

LeetCode의 `class Solution` 메서드를 일반 함수로 변환합니다:
- `class Solution:` 제거
- `def twoSum(self, ...)` → `def two_sum(...)` (camelCase → snake_case, self 제거)
- Type hint 변환: `List[int]` → `list[int]`, `Optional[TreeNode]` → `TreeNode | None`
- `from typing import ...` 제거

### Step 4: 소스 파일 생성

파일: `src/leetcode/{snake_case_title}_{번호}.py`

```python
"""
{번호}. {제목}
https://leetcode.com/problems/{titleSlug}/

Difficulty: {난이도}

문제 설명:
    {content를 텍스트로 변환하여 정리}

제약 조건:
    {constraints 정리}
"""

# 자료구조 필요시 import

def {함수명}({파라미터}) -> {반환타입}:
    raise NotImplementedError
```

### Step 5: 테스트 파일 생성

파일: `test/leetcode/test_{snake_case_title}_{번호}.py`

- pytest + parametrize 사용
- GraphQL 응답의 `content`에서 Example 입출력을 파싱하여 테스트 케이스 생성
- 자료구조 필요시 헬퍼 함수 import

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
