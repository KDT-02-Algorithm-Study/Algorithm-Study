# 2468 안전영역
# 31256KB 632ms 874B

import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

def dfs(x, y):
    st = [(x, y)]
    visited[x][y] = True
    while st:
        x, y = st.pop()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] > h:
                st.append((nx, ny))
                visited[nx][ny] = True

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
M = max(map(max, graph))
m = min(map(min, graph))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

a = 0
for h in range(m-1, M):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
                if graph[i][j] > h and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
    a = max(a, cnt)

print(a)