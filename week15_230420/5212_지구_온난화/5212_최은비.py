# 지구 온난화 https://www.acmicpc.net/problem/5212
# 34208KB / 68ms
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
ground = deque()
sea = []
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'X':
            ground.append((i, j))

# 땅인 부분을 모두 순회하면서 주위에 바다가 몇칸인지 카운트
while ground:
    cnt = 0
    x, y = ground.popleft()
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < r and 0 <= ny < c:
            if grid[nx][ny] == '.':
                cnt += 1
        else:
            cnt += 1

    if cnt > 2:
        sea.append((x, y))

for i, j in sea:
    grid[i][j] = '.'

# 섬인 부분을 찾기 위한 리스트
map_r = []
map_c = []

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'X':
            map_r.append(i)
            break

for i in range(c):
    for j in range(r):
        if grid[j][i] == 'X':
            map_c.append(i)
            break

for i in range(min(map_r), max(map_r)+1):
    for j in range(min(map_c), max(map_c)+1):
        print(grid[i][j], end='')
    print()
