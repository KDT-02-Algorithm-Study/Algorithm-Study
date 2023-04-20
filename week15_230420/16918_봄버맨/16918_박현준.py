# 34520 KB / 1884 ms

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_bomb():
    for x in range(R):
        for y in range(C):
            if grid[x][y] == 'O':
                bombs.append((x, y))

def bomb_plant():
    for x in range(R):
        for y in range(C):
            if grid[x][y] == '.':
                grid[x][y] = 'O'

def bomb_explode():
    for x, y in bombs:
        grid[x][y] = '.'
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < R and -1 < ny < C:
                grid[nx][ny] = '.'

# 폭탄 설치 (기본)
# 1초 멈춤
# 모든 칸에 폭탄 설치
# 1초 멈춤
# 모든 칸의 폭탄 폭발

R, C, N = map(int, input().split())
grid = [[x for x in input()] for _ in range(R)]

N -= 1
while N:
    bombs = deque([])
    find_bomb()
    bomb_plant()
    N -= 1
    if N == 0:
        break
    bomb_explode()
    N -= 1

for g in grid:
    print(''.join(g))