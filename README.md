# BOJ Solutions

태블릿 + Termux + Vim 환경에서 풀이한 백준 문제를 정리합니다.  
- **Language**: Python 3  
- **Env**: Termux (Android), Vim  
- **Goal**: 골드 이상 100문제 풀이 & 정리

# 구조i


## 사용법
```bash
# 템플릿 복사해서 새 문제 시작
cp templates/solve_template.py gold4/1167_tree_diameter/main.py

# 로컬 실행 (input.txt를 표준입력으로 연결)
./scripts/run_local.sh gold4/1167_tree_diameter


---

# NOTES.md (개인 메모/실수/회고)
```md
# 문제별 메모 / 실수 기록

> 자유롭게 적는 공간 (남 보여주는 용도 X)

## 공통 실수 체크리스트
- [ ] 입력 파싱(-1, 공백/개행 처리)
- [ ] 1-index vs 0-index 혼동
- [ ] visited 초기화/재사용
- [ ] INF 값 충분히 크게
- [ ] 재귀 깊이/스택 제한 (sys.setrecursionlimit)
- [ ] 시간복잡도 추정과 실제 차이
- [ ] 디버깅용 출력 제거

---

## 1167 트리의 지름
- 처음 DFS 한 번만 돌려서 오답 → BFS 2번 필요.
- 입력 줄 끝의 `-1` 처리 누락으로 파싱 실패.

## 1504 특정한 최단 경로
- 다익스트라 3회(1→v1, 1→v2, v1↔v2) 필요.
- 경로 두 가지(1→v1→v2→N, 1→v2→v1→N) 비교해야 함.
- 우선순위큐 push 조건 누락해서 TLE 발생했었음

#ex .
