import sys
from collections import deque

def bfs(y, x):
    q = deque([[(y, x)]])
    check[y][x] = True
    cnt = 0

    while 1:
        q.append([])
        cnt += 1
        for y, x in q.popleft():
            for a in range(3):
                for b in range(3):
                    if 0 <= y+dy[a] < n and 0 <= x+dx[b] < m and not check[y+dy[a]][x+dx[b]]:
                        if space[y+dy[a]][x+dx[b]]:
                            return cnt
                        else:
                            check[y+dy[a]][x+dx[b]] = True
                            q[0].append((y+dy[a], x+dx[b]))


n, m = map(int, input().split())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 0, 1]
dy = [-1, 0, 1]
safe = []

for i in range(n):
    for j in range(m):
        if not space[i][j]:
            check = [[False]*m for _ in range(n)]
            safe.append(bfs(i, j))

print(max(safe))