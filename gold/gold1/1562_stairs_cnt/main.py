import sys
input = sys.stdin.readline

MOD = 1_000_000_000

def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    N = int(input())
    if N < 10  :
        print(0)
        exit()

    #dp[length][last_diti][mask]
    dp = [[[0]*(1<<10) for _ in range(10)] for _  in range(N+1)]

    for i in range(1,10):
        dp[1][i][1<<i] = 1

    for length in range(2,N+1):
        for last in range(10):
            for mask in range(1<<10):
                if dp[length -1 ][last][mask] == 0:
                    continue
                cur = dp[length-1][last][mask]

                if last > 0 :
                    dp[length][last-1][mask | (1<< (last-1))] += cur
                    dp[length][last-1][mask | (1<< (last-1))] %= MOD
                if last < 9 : 
                    dp[length][last+1][mask | (1<< (last+1))] += cur
                    dp[length][last+1][mask | (1<< (last+1))] %= MOD

    FULL_MASK = (1 <<10) -1 
    result = 0
    for last in range(10):
        result = ( result + dp[N][last][FULL_MASK]) % MOD 
                
    print(result)
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
