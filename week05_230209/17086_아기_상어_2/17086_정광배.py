# 17086 아기 상어 2
import sys
from collections import deque
input = sys.stdin.readline

def bfs(q:deque, x, y):
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not d[nx][ny]:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

q = deque()
for x in range(n):
    for y in range(m):
        if d[x][y] == 1:
            q.append((x,y))
bfs(q,x,y)
print(max(map(max, d))-1)