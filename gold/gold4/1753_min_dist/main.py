import sys
input = sys.stdin.readline
import heapq

def dijkstra(V,E,start,edge):
    INF = 10**9
    min_dist = [INF]*(V+1) 
    min_dist[start] = 0
    
    heap = []
    heapq.heappush(heap,(0,start)) # (dist,node)
    while heap:
        cur_dist , cur_node = heapq.heappop(heap)
        if cur_dist > min_dist[cur_node]:
            continue

        for next_node,weight in edge[cur_node]:
            new_dist = cur_dist + weight
            if new_dist <  min_dist[next_node]:       
                min_dist[next_node] = new_dist
                heapq.heappush(heap,(new_dist,next_node))
                
    for p in range(V):
        if min_dist[p+1] == INF:
            print("INF")
        else:
            print(min_dist[p+1])
def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    V,E = map(int,input().split())
    start = int(input())
    edge = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v,w = map(int,input().split())
        edge[u].append((v,w)) 
    dijkstra(V,E,start,edge)
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
