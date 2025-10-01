import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def dfs(node, cnt, graph, visited):
    visited[node] = cnt
    for nxt in graph[node]:
        if visited[nxt] == 0:
            dfs(nxt, cnt, graph, visited)

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            dfs(i, cnt, graph, visited)

    print(cnt)

if __name__ == "__main__":
    solve()
