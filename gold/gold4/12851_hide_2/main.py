import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    N,K = map(int,input().split())
    MAX = 100000
    visited = [-1] * (MAX+1)
    count=[0]*(MAX +1) 
    queue = deque([N])
    visited[N] = 0 
    count[N] = 1
    
    while queue:
        x = queue.popleft()
        
        for nx in (x-1,x+1,x*2):
            if 0 <= nx <= MAX:
                if visited[nx] == -1:
                    visited[nx] = visited[x]+1
                    count[nx] = count[x]
                    queue.append(nx)
                elif visited[nx] == visited[x]+1:
                    count[nx] += count[x]
    print(visited[K])
    print(count[K])
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
