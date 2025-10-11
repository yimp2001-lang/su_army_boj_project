import sys
input = sys.stdin.readline
INF = 10**6
def make_dp(dp,city):
    cost,cnt = city[1],city[2]
    cur = 1
    while cur < len(dp):
        if cur % cnt ==0 :
            new_dp = (cur//cnt)*cost
        else:
            new_dp = (cur//cnt+1 ) * cost
        if cur-cnt >=1:
            dp[cur] = min(new_dp ,dp[cur], dp[cur-cnt] + dp[cnt] )
        else:
            dp[cur] = min(new_dp ,dp[cur])
        cur+=1


def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    C,N = map(int,input().split())
    city = list()
    dp = [INF]*(C+1)
    for _ in range(N):
        cost,cnt = map(int,input().split())
        per = cnt/cost
        city.append((per,cost,cnt))
    city.sort(key=lambda x : (-x[0],-x[1]))
    for i in range(N):
        make_dp(dp,city[i])
    print(dp[C])
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
