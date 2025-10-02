처음부터 삼각형 구조를 보고 DFS,BFS 구조인 거라고 잘못 생각을 고정하고 시작 
점차 생각하면서 DP로 문제를 해결했음 
DP인데 이게 DFS이라고 하는게 맞나 싶어서 gpt한테 물어봤더니 함수명을 DFS라고 쓰면 안될 것 같다고 지적. DP방법이니 재귀보다 반복문을 쓰는게 가독성이 더 좋다고 함
그래서 수정함 

처음 코드 


import sys
input = sys.stdin.readline

def DFS(N, nums):
    if N == 0:
        return nums[0][0]
    else:
        N -= 1
        for i in range(N):
            nums[N-1][i] += max(nums[N][i], nums[N][i+1])
        return DFS(N, nums)

def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    print(DFS(N, nums))

if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
