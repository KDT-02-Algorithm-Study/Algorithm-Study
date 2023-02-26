# 1926 그림

import sys
input = sys.stdin.readline

def dfs(x, y):
    cnt = 0
    stack = [(x, y)]
    d[x][y] = 2
    cnt += 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] == 1:
                    stack.append((nx, ny))
                    d[nx][ny] = 2
                    cnt += 1
    return cnt
n, m = map(int,input().split())
d = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
total = 0
for x in range(n):
    for y in range(m):
        if d[x][y] == 1:
            total += 1
            cnt = dfs(x, y)
            result = max(result, cnt)
print(total, result,sep='\n')