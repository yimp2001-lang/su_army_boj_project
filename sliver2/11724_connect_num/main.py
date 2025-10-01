import sys
input = sys.stdin.readline

def find_connect(N,cnt,l,r,edge,visited):
    if visited[r] != 0 :
        return
    else:
        visited[r] = cnt
        for new_r in range(N+1):
            if edge[r][new_r] != 0:
                find_connect(N,cnt,r,new_r,edge,visited)


def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    N,M = map(int,input().split())
    visited = [0]*(N+1)
    edge = [[0]*(N+1) for _ in range(N+1)]
    result = 0
    for _ in range(M):
        l,r = map(int,input().split())
        edge[l][r] = 1
        edge[r][l] =1


    for l in range(N+1):
        for r in range(N+1):
            if edge[l][r] == 0 :
                continue
            else:
                if visited[l] == 0:
                    visited[l]=1
                    result+=1
                    find_connect(N,result,l,r,edge,visited)
                else:
                    continue
    print(result)


if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    sys.setrecursionlimit(1_000_000)
    solve()
