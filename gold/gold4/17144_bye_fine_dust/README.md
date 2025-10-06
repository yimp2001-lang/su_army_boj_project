다 풀고 예시까지 잘 디버깅해서 맞춤 
근데 반복되는 구조가 많아서 함수화 하고 싶기도 하고 함수가 너무 더러워서 바꾸고 싶었음 
chat gpt가 구조만 바꿔준 코드

import sys
input = sys.stdin.readline

# 확산 (Diffusion)
def diffuse(room, R, C):
    temp = [[0] * (C + 2) for _ in range(R + 2)]
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if room[r][c] > 0:
                spread = room[r][c] // 5
                cnt = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if room[nr][nc] != -2 and room[nr][nc] != -1:
                        temp[nr][nc] += spread
                        cnt += 1
                room[r][c] -= spread * cnt

    for r in range(1, R + 1):
        for c in range(1, C + 1):
            room[r][c] += temp[r][c]


# 정화 (Purification)
def purify_cycle(room, sr, sc, dirs):
    prev = 0
    r, c = sr, sc + 1
    for dr, dc in dirs:
        while True:
            nr, nc = r + dr, c + dc
            if room[nr][nc] == -1:
                return
            if not (1 <= nr < len(room) - 1 and 1 <= nc < len(room[0]) - 1):
                break
            room[nr][nc], prev = prev, room[nr][nc]
            r, c = nr, nc


def purify(room, air_c, R, C):
    upper_dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 반시계
    lower_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 시계
    purify_cycle(room, air_c[0][0], air_c[0][1], upper_dirs)
    purify_cycle(room, air_c[1][0], air_c[1][1], lower_dirs)


# 메인 로직
def solve():
    R, C, T = map(int, input().split())
    room = [[-2] * (C + 2) for _ in range(R + 2)]
    air_c = []

    for i in range(R):
        line = list(map(int, input().split()))
        for j in range(C):
            room[i + 1][j + 1] = line[j]
            if line[j] == -1:
                air_c.append((i + 1, j + 1))

    for _ in range(T):
        diffuse(room, R, C)
        purify(room, air_c, R, C)

    # 남은 미세먼지 합산
    result = sum(sum(cell for cell in row if cell > 0) for row in room)
    print(result)


if __name__ == "__main__":
    solve()
