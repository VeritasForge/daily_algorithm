---
description: 변경사항을 커밋하고 원격 저장소로 푸시합니다.
allowed-tools: Bash, Read, Grep, Glob
---

# Commit & Push Changes

변경사항을 커밋하고 원격 저장소로 푸시합니다.

**Usage:**
- `/commit` — 모든 변경사항 커밋
- `/commit <message>` — 커스텀 메시지로 모든 변경사항 커밋
- `/commit <file_path>` — 해당 파일과 대응하는 src/test 파일만 커밋
- `/commit <file_path> <message>` — 해당 파일 쌍을 커스텀 메시지로 커밋

```
Parse the user's input from: $ARGUMENTS

## Step 0: Parse Arguments

$ARGUMENTS를 분석하여 **파일 경로**와 **커밋 메시지**를 분리합니다.

### 파일 경로 감지

인자 중 다음 패턴에 해당하는 것을 파일 경로로 인식합니다:
- `src/` 또는 `test/`로 시작하는 경로
- `.py`로 끝나는 경로

### 대응 파일 매핑

파일 경로가 감지되면, 소스-테스트 쌍을 자동으로 구성합니다:

| 입력 파일 | 대응 파일 |
|-----------|-----------|
| `src/leetcode/{name}.py` | `test/leetcode/test_{name}.py` |
| `test/leetcode/test_{name}.py` | `src/leetcode/{name}.py` |
| `src/common/{name}.py` | `test/common/test_{name}.py` |
| `test/common/test_{name}.py` | `src/common/{name}.py` |

**규칙:**
- 대응 파일이 실제로 존재하는 경우에만 쌍에 포함합니다 (`ls` 또는 `git status`로 확인)
- 파일 경로가 감지되지 않으면 기존처럼 **모든 변경사항**을 대상으로 합니다
- 나머지 인자는 커밋 메시지로 사용합니다

### 커밋 메시지

- 파일 경로를 제외한 나머지 텍스트가 있으면 커스텀 커밋 메시지로 사용합니다
- 없으면 Step 2에서 자동 생성합니다

## Step 1: Check Status

Run the following commands in parallel:
- `git status` (never use -uall flag)
- `git diff HEAD` (or `git diff --cached` if no commits exist yet)
- `git log --oneline -5` (to follow existing commit style)

If there are no changes (working tree clean, nothing staged), report:
  "변경사항이 없습니다. Working tree is clean."
and stop.

## Step 2: Generate Commit Message

변경된 파일을 분석하여 커밋 유형을 판단합니다.

### Case A: LeetCode 문제 커밋

변경된 파일이 `src/leetcode/` 또는 `test/leetcode/`에 있는 경우:

**형식:** `[leetcode][{difficulty}] {number}. {Problem Name}`

1. **파일명에서 정보 추출**:
   - `src/leetcode/combination_sum_39.py` → 번호: 39, 이름: Combination Sum
   - 파일명 규칙: `{snake_case_name}_{number}.py`
   - snake_case를 Title Case로 변환 (각 단어 첫 글자 대문자)

2. **난이도 감지** (우선순위):
   - 소스 파일 상단 주석/독스트링에서 `Difficulty: Easy/Medium/Hard` 검색
   - 소스 파일의 LeetCode URL로 난이도 확인
   - 감지 실패 시 사용자에게 질문

3. **예시**:
   - `[leetcode][easy] 206. Reverse Linked List`
   - `[leetcode][medium] 39. Combination Sum`
   - `[leetcode][hard] 42. Trapping Rain Water`

### Case B: 일반 커밋

LeetCode 문제가 아닌 변경사항:

**형식:** 변경 내용을 간결하게 서술

- 예: `add tree utility to src/common`
- 예: `update CLAUDE.md with new conventions`
- 예: `fix linked list helper edge case`

## Step 3: Stage & Commit

### Staging

**파일 경로가 지정된 경우 (Step 0에서 감지):**
- Step 0에서 구성한 파일 쌍만 `git add`합니다
- 예: `git add src/leetcode/maximum_subarray_53.py test/leetcode/test_maximum_subarray_53.py`

**파일 경로가 지정되지 않은 경우:**
- 변경된 파일을 개별적으로 staging 합니다 (`git add .` 사용 금지)

`.env`, credentials 등 민감한 파일은 제외합니다.

HEREDOC 형식으로 커밋합니다:

**Case A (LeetCode 문제 커밋):** Co-Authored-By 없이 커밋합니다.

git commit -m "$(cat <<'EOF'
{commit message}
EOF
)"

**Case B (일반 커밋):** Co-Authored-By를 포함합니다.

git commit -m "$(cat <<'EOF'
{commit message}

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"

## Step 4: Push

원격 저장소로 push 합니다:
- upstream이 설정된 경우: `git push`
- upstream이 없는 경우: `git push -u origin <current-branch>`

push 실패 시 에러를 보고하고 다음을 제안합니다:
  git pull --rebase && git push

## Step 5: Report

결과를 보고합니다:

**Commit:** <commit message>
**Branch:** <branch name>
**Files Changed:** <count> files (+<additions>, -<deletions>)
**Remote:** pushed to origin/<branch>
```
