import sys
input = sys.stdin.readline

<<<<<<< HEAD
=======
def max_sum(N,nums):
    while N != 0:
        N-=1 
        for i in range(N):
            nums[N-1][i] += max(nums[N][i],nums[N][i+1])

    return nums[0][0]

>>>>>>> 4bb105e (feat : solve 1932_N_tri (DP))
def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
<<<<<<< HEAD
    pass
=======
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    print(max_sum(N,nums)) 

>>>>>>> 4bb105e (feat : solve 1932_N_tri (DP))

if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
