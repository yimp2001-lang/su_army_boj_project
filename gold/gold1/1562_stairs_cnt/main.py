import sys
input = sys.stdin.readline

MOD = 1_000_000_000

def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    N = int(input())
    # 10 미만의 숫자는 0~9까지의 숫자를 모두 쓸 수 없으므로 0처리 
    if N < 10  :
        print(0)
        exit()

    #dp[length][last_diti][mask] 3차원 DP 생성
    dp = [[[0]*(1<<10) for _ in range(10)] for _  in range(N+1)]

    #길이가 1일 때부터 DP를 확장할 것이므로 길이가 1일 때 해당 숫자 DP값에 1이라고 초기화  
    for i in range(1,10):
        dp[1][i][1<<i] = 1

    # 길이가 2일 때부터 N까지 DP를 확장 
    for length in range(2,N+1):
        # 맨 숫자는 0~9까지 가능, 맨 숫자가 뭐인지에 따라 길이의 DP를 구분
        for last in range(10):
            # mask를 0부터 9까지 10개의 숫자 중 무엇을 추가해도 상관없는지 확인 하기 위함 
            for mask in range(1<<10):
                # 해당 DP가 조건을 만족하지 않는 경우 계산의 효율성을 위해 처음부터 조건문으로 돌림
                if dp[length -1 ][last][mask] == 0:
                    continue

                cur = dp[length-1][last][mask]
                # 전 길이의 last가 0보다 클 때 last-1을 뒤로 붙이는 형식 876 이면 8765 , 그리고 해당 DP에 전에 있던 DP값을 더하고 MOD로 나머지만 구해준다
                # 마지막이 0인 부분일 때 -1 하는 경우를 제외시켜줌
                if last > 0 :
                    dp[length][last-1][mask | (1<< (last-1))] += cur
                    dp[length][last-1][mask | (1<< (last-1))] %= MOD
                # 전 길이의 last가 9보다 작을 때 last+1을 뒤로 붙이는 형식 876 이면 8767 , 그리고 해당 DP에 전에 있던 DP값을 더하고 MOD로 나머지만 구해준다
                # 마지막이 9인 부분일 때 +1 하는 경우를 제외시켜줌
                if last < 9 : 
                    dp[length][last+1][mask | (1<< (last+1))] += cur
                    dp[length][last+1][mask | (1<< (last+1))] %= MOD

    FULL_MASK = (1 <<10) -1 
    result = 0
    for last in range(10):
        # FULL MASK로 길이가 N이고 last가 0에서 9까지 FULL MASK 다 있는 경우 다 더해서 result 값을 구한다. 
        result = ( result + dp[N][last][FULL_MASK]) % MOD 
                
    print(result)
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
