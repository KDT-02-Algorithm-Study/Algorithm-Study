from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def global_warming(x, y):
    cnt = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            cnt += 1
        elif grid[nx][ny] == '.':
            cnt += 1
    if cnt >= 3:
        island.append((x, y))

def sink():
    for _ in range(len(island)):
        x, y = island.popleft()
        grid[x][y] = '.'

R, C = map(int, input().split())

grid = [[x for x in input()] for _ in range(R)]

island = deque()

while True:
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'X':
                global_warming(i, j)
    if len(island) == 0:
        break
    sink()
    print(grid)
    print()