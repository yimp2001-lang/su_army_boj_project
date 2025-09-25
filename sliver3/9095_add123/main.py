import sys
input = sys.stdin.readline

def add_123(N):
    dp = [0] * 11
    dp[1],dp[2],dp[3]= 1,2,4
    
    for i in range(4,N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[N]

def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(add_123(N))
     
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
