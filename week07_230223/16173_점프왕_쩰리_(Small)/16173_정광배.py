# 16173 점프왕 쩰리 (Small)
# 31256KB 40ms 591B
import sys
sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

def dfs(x, y):
    s = [(x, y)]
    while s:
        x, y = s.pop()
        j = graph[x][y]
        if j == -1:
            return True
        visited[x][y] = True
        if j == 0:
            continue
        nx = x+j
        ny = y+j
        if nx < n and not visited[nx][y]:
            s.append((nx, y))
        if ny < n and not visited[x][ny]:
            s.append((x, ny))
    return False

n = int(input())

graph= [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

if dfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')