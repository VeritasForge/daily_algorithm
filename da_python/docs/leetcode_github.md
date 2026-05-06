# LeetCode에서 Git과 비슷한 문제들

LeetCode에는 "Git을 그대로 구현해라"라는 문제는 없지만, **Git의 핵심 메커니즘**을 부분별로 닮은 문제들이 흩어져 있다. Git의 어떤 기능이 어떤 문제에 매핑되는지로 정리한다.

## 🗺️ Git 개념 ↔ LeetCode 매핑 표

| Git 기능 | 현실 비유 | LeetCode 문제 | 난이도 | 핵심 아이디어 |
|---|---|---|---|---|
| `git commit` (스냅샷) | 사진 앨범에 한 장씩 추가 | **1146. Snapshot Array** | Medium | 변경된 인덱스만 `(snap_id, value)`로 저장 → 이진 탐색으로 조회 |
| `git checkout <time>` | 특정 날짜의 일기장 펴기 | **981. Time Based Key-Value Store** | Medium | 타임스탬프별 값 저장, 이진 탐색으로 "그 시점 직전 값" 찾기 |
| `git merge-base` (공통 조상) | 가족 족보에서 공통 할아버지 찾기 | **236. LCA of a Binary Tree** | Medium | 트리에서 두 노드의 가장 낮은 공통 조상 |
| `git merge-base` (부모 포인터) | 부모 손잡고 거슬러 올라가기 | **1650. LCA III** (부모 포인터) | Medium | 두 링크드리스트 교차점 찾기와 동형 |
| `git bisect` (이진 탐색으로 버그 커밋 찾기) | 책에서 처음 잘못된 페이지 찾기 | **278. First Bad Version** | Easy | 단조성을 이용한 이진 탐색 — bisect의 정확한 모델 |
| `git diff` (차이 비교) | 두 그림 틀린 그림 찾기 | **1143. Longest Common Subsequence** | Medium | diff 알고리즘의 핵심 (LCS 기반) |
| `git diff` (편집 거리) | 단어 고치기 최소 횟수 | **72. Edit Distance** | Hard | Myers diff의 이론적 기반 |
| `git ls-tree` / 파일 시스템 | 폴더 트리 만들기 | **588. Design In-Memory File System** ⭐ | Hard (premium) | mkdir/ls/addContent — Git의 tree object와 유사 |
| 경로 기반 트리 | 우편 주소 체계 | **1166. Design File System** | Medium (premium) | 경로 → 값 매핑 (Trie 기반) |
| 버전 번호 비교 | "v1.2.3 vs v1.10.0" | **165. Compare Version Numbers** | Medium | semver 비교 |

## 🎯 가장 추천하는 학습 순서

성장을 고려한 **개념 난이도 순** 학습 경로:

```
1단계: 278. First Bad Version          ← git bisect 감 잡기 (Easy)
   ↓
2단계: 1146. Snapshot Array            ← commit의 핵심 자료구조 (Medium)
   ↓
3단계: 981. Time Based Key-Value Store ← checkout/HEAD 개념 (Medium)
   ↓
4단계: 236. LCA of a Binary Tree       ← merge-base (Medium)
   ↓
5단계: 1143. Longest Common Subsequence ← diff 원리 (Medium)
   ↓
6단계: 1166. Design File System         ← Git tree object (Medium, premium)
```

## 💡 가장 직접적인 "Git스러운" 문제 — 1146. Snapshot Array

이 문제가 Git과 가장 닮은 이유:

- **Git의 트릭**: 파일이 안 바뀌면 새로 저장하지 않고, 이전 객체를 참조만 함 (content-addressable storage)
- **1146의 트릭**: 인덱스마다 `(snap_id, value)` 변경 이력만 저장 → 매 snapshot마다 전체 복사하지 않음
- 둘 다 핵심은 **"변경분만 저장하고 이진 탐색으로 시점 복원"**

```
Git:                       Snapshot Array:
commit3 ─→ blob_v3         idx[i] = [(0, "a"), (5, "b"), (12, "c")]
commit2 ─→ blob_v3 (참조)             ↑
commit1 ─→ blob_v1                   snap_id=7 조회 시 이진 탐색 → "b" 반환
```

## 🚫 추가로 확인할 점

- **Premium 문제** (588, 1166)는 무료 계정에서 안 보일 수 있음 → LeetCode 검색창에 번호 직접 입력하면 일부 노출됨
- **"Git을 처음부터 끝까지 구현"** 같은 문제는 LeetCode에 없음 → 그건 **CodeCrafters의 "Build Your Own Git"** 챌린지가 정답 (LeetCode 영역 밖)

## 📚 참고 자료

- [Encountering the idea of Git in a Leetcode problem (1146 분석)](https://medium.com/@iggeehu/encountering-the-idea-of-git-in-a-leetcode-problem-41846bdc16ba)
- [1146. Snapshot Array — LeetCode](https://leetcode.com/problems/snapshot-array/)
- [165. Compare Version Numbers — algo.monster](https://algo.monster/liteproblems/165)
- [First Bad Version — LeetCode](https://leetcode.com/problems/first-bad-version/)
