import sys
input = sys.stdin.readline
from itertools import combinations

def make_dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    N,M = map(int,input().split())
    city = [[-1]*(N+1) for _ in range(N+1)]
    house_cnt = 0
    chicken_cnt =0  
    house = list()
    chicken = list()
    result = 9999999

    for i in range(1,N+1):
        line = list(map(int,input().split()))
        for j in range(1,N+1):
            city[i][j] = line[j-1] 
            if city[i][j] == 1:
                house_cnt +=1
                house.append((i,j))
            elif city[i][j] == 2 :
                chicken_cnt +=1
                chicken.append((i,j))
            else:
                continue
    dist = [[-1]*(chicken_cnt+1) for _ in range(house_cnt+1)]
    
    for i in range(1,house_cnt+1):
        for j in range(1,chicken_cnt+1):
            dist[i][j] = make_dist(house[i-1],chicken[j-1])

    for chicken_combo in combinations(range(1,chicken_cnt+1),M): 
        total = 0 
        for h in range(1,house_cnt+1):
            min_d = 99999
            for c in  chicken_combo:
                min_d = min(min_d,dist[h][c])
            total+=min_d
        result = min(result,total)        
    print(result)
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
