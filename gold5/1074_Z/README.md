처음 생각처음 생각처음 생각

r행 c 열을 몇 번 째 방문인지 이니깐 
r,c일 때 숫자가 뭐인지 알아야함 그러면 몇 번 째 방문했는지 알 수 있을 듯 
숫자 +1 하면 되니깐 

r에서의 규칙 
숫자 : 0 2 8 10 32 34 40 42
열    :  0 1 2 3   4    5   6    7    8    

0 2 4 8 일 때 2^(r-1)의 수가 나옴  
4 16 
5 32
6 64
7 128 

그래서 r을 받았을 때 
2의 거듭 제곱인지 확인 -> 함수로 따로 빼서 1이 될 때까지 나머지가 계속 0이면 true 아니면 false return 시키기 
reutrn할 때 지금까지의 몇 번 2로 나눴는지하고 나머지도 빼기

2의 거듭 제곱이면  2^(r-1) 일단 결과값으로 저장 

아니면 2^(몇 번 나눈지) +

##흠 근데 문제를 푸니깐 재귀로도 풀 수 있을 것 같기도하고 

오 4로 나눴을 때 4개의 나머지가 같음을 발결 
0 1 
2 3 

크게 확장해서 


import sys
input = sys.stdin.readline

def make_result(N, r, c, result):
    if N == 0:
        return 0
    half = 2**(N - 1)
    num = half * half
    if r >= half and c >= half:
        result += 3 * num
        r -= half
        c -= half
    elif r >= half and c < half:
        result += 2 * num
        r -= half
    elif r < half and c >= half:
        result += 1 * num
        c -= half
    else:
        result += 0 * num
    make_result(N - 1, r, c, result)

def solve():
    N, r, c = map(int, input().split())
    result = 0
    make_result(N, r, c, result)
    print(result)

if __name__ == "__main__":
    # sys.setrecursionlimit(1_000_000)
    solve()

#fist code 
