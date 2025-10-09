import sys
input = sys.stdin.readline
import heapq

def dijkstra(V,E,start,edge):
    # 각 거리 초기화
    INF = 10**9
    min_dist = [INF]*(V+1) 
    min_dist[start] = 0

    # 우선순위 큐 (최소 힙)
    heap = []
    heapq.heappush(heap,(0,start)) # (dist,node)
    
    while heap:
        #현재까지 가장 짧은 거리의 노드를 꺼냄 
        cur_dist , cur_node = heapq.heappop(heap)
        # 이미 더 짧은 경로로 방문한 적이 있다면 continue
        if cur_dist > min_dist[cur_node]:
            continue

        # 현재 노드에서 다음 노드와 거리를 꺼내서 다익스트라 진행 
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
