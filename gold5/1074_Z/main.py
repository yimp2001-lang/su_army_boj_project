import sys
input = sys.stdin.readline

def make_result(N,r,c,result):
    if N==0:
        return result
    half = 2**(N-1)
    num = half * half
    quad = 0 
    if r >= half :
        quad+=2
        r-=half
    if c >= half:
        quad+=1
        c-=half
    result+= quad*num
    return make_result(N-1,r,c,result)

def solve():
    # TODO: 여기부터 로직
    # 예시:
    N,r,c = map(int,input().split())
    print(make_result(N,r,c,0))

    # n = int(input())
    # arr = list(map(int, input().split()))

if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
