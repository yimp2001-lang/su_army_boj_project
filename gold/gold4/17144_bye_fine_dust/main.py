import sys
input = sys.stdin.readline

def diffuse(R,C,room,directs,temp):
    for i in range(1,R+1):
        for j in range(1,C+1):
            if room[i][j] > 0:  
                dust = room[i][j]//5
                for direct in directs: 
                    r = i+direct[0] 
                    c = j+direct[1]
                    if room[r][c] >= 0 :
                        room[i][j] -= dust
                        temp[r][c] += dust
                    
    for i in range(1,R+1):
        for j in range(1,C+1):
            room[i][j] += temp[i][j]

def purify(R,C,air_c,room):
    upper_purify(R,C,air_c[0],room)
    down_purify(R,C,air_c[1],room)

def upper_purify(R,C,air_c,room):
    start_r = air_c[0]
    start_c = air_c[1]
    temp_1 = room[start_r][start_c+1]
    room[start_r][start_c+1] = 0
    for dc in range(2,C):
        temp_2 = room[start_r][dc+1]
        room[start_r][dc+1] = temp_1
        temp_1 = temp_2
    for dr in range(start_r,1,-1):
        temp_2 = room[dr-1][C]
        room[dr-1][C] = temp_1
        temp_1 = temp_2
    for dc in range(C,1,-1):
        temp_2 = room[1][dc-1]
        room[1][dc-1] = temp_1
        temp_1 = temp_2
    for dr in range(1,start_r):
        temp_2 = room[dr+1][1]
        room[dr+1][1] = temp_1
        temp_1 = temp_2
    room[start_r][start_c] = -1
    return

def down_purify(R,C,air_c,room):
    start_r = air_c[0]
    start_c = air_c[1]
    temp_1 = room[start_r][start_c+1]
    room[start_r][start_c+1] = 0
    for dc in range(2,C):
        temp_2 = room[start_r][dc+1]
        room[start_r][dc+1] = temp_1
        temp_1 = temp_2 
    for dr in range(start_r,R):
        temp_2 = room[dr+1][C]
        room[dr+1][C] = temp_1
        temp_1 = temp_2
    for dc in range(C,1,-1):
        temp_2 = room[R][dc-1]
        room[R][dc-1] = temp_1
        temp_1 = temp_2
    for dr in range(R,start_r,-1):
        temp_2 = room[dr-1][1]
        room[dr-1][1] = temp_1
        temp_1 = temp_2
    room[start_r][start_c] = -1 
    return 

def print_matrix(matrix):
    for row in matrix:
        print(", ".join(map(str,row)))
def solve():
    # TODO: 여기부터 로직
    # 예시:
    # n = int(input())
    # arr = list(map(int, input().split()))
    R,C,T = map(int,input().split())

    room = [[-2]*(C+2) for _ in range(R+2)]
    air_c = list()
    for i in range(R):
        line = list(map(int,input().split()))
        for j in range(C):
                    if line[j] == -1:
                        air_c.append((i+1,j+1))
                    room[i+1][j+1] = line[j] 
     
    directs = [(-1,0),(0,1),(1,0),(0,-1)]
    for i in range(T): 
        temp = [[0]*(C+2) for _ in range(R+2)]
        #test
        #print_matrix(room)
        diffuse(R,C,room,directs,temp)
        #test 
        #print_matrix(room)
        purify(R,C,air_c,room)
        #test
        #r = 0 
        #for row in room:
        #    r += sum(row[i] for i in range(C+2) if row[i]>0)
        #print("log",i," : ",r)
    #print_matrix(room)
    result = 0 
    for row in room:
        result+= sum(row[i] for i in range(C+2) if row[i]>0)

    print(result)
if __name__ == "__main__":
    # 필요 시 재귀 한도 상향
    # sys.setrecursionlimit(1_000_000)
    solve()
