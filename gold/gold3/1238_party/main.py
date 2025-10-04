import sys
import heapq
input = sys.stdin.readline
INF = 10**9

def dijkstra(N,start,times):
    dist = [INF]*N
    dist[start] = 0 
    heap = [(0,start)] #dist and node 

    while heap:
        cur_dist,cur = heapq.heappop(heap)
        if cur_dist > dist[cur]:
            continue

        for nxt_cur, nxt_dist  in times[cur]:
            if cur_dist + nxt_dist < dist[nxt_cur]:
                dist[nxt_cur] = cur_dist + nxt_dist
                heapq.heappush(heap,(dist[nxt_cur],nxt_cur))

    return dist

def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    
    #initial
    N,M,X =  map(int,input().split())
    X-=1
    times = [[] for _ in range(N)]

    for _ in range(M):
        start , end , time = map(int,input().split())
        times[start-1].append((end-1,time))
    back_path = [0]*(N)
    
    go_path = dijkstra(N,X,times)
    for i in range(N):
        back_path[i] = dijkstra(N,i,times)[X]
    print(max(go_path[i]+back_path[i] for i in range(N)))

if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
