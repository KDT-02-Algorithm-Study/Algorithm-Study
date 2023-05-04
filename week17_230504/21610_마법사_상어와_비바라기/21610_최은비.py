# 마법사 상어와 비바라기 https://www.acmicpc.net/problem/21610
# 34240KB / 408ms

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
delta = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
copy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
cloud = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])

for _ in range(m):
    d, s = map(int, input().split())
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    # 구름 이동
    for __ in range(len(cloud)):
        x, y = cloud.popleft()
        nx = (x + delta[d][0] * s) % n
        ny = (y + delta[d][1] * s) % n
        cloud.append((nx, ny))
        # 구름이 있는 칸의 물 1 증가
        grid[nx][ny] += 1

    for x, y in cloud:
        visited[x][y] = True

        # 물 복사
        cnt = 0
        for dx, dy in copy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] > 0:
                    grid[x][y] += 1

    cloud = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 1 and not visited[i][j]:
                visited[i][j] = True
                grid[i][j] -= 2
                cloud.append((i, j))

ans = 0
for i in range(n):
    ans += sum(grid[i])

print(ans)