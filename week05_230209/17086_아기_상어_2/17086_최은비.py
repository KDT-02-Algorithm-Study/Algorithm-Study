# 아기 상어 2 https://www.acmicpc.net/problem/17086
# 접근법
# 1. 상어 위치부터 BFS 시작, 상어가 없는 곳은 상어로부터 거리로 값을 바꾼다.
# 2. 상어도 아니고 0도 아닌 값은 이미 다른 상어로부터의 거리를 뜻한다.
#    다른 상어로부터 거리와 현재 상어로부터 거리를 비교해서 더 작은 값으로 바꾼다.
#    (그 칸과 가장 가까운 상어와의 거리니까 작은 값으로 바꿔야 함)
# 3. 모든 상어로부터 탐색을 마친 후 최대값을 구한다.(시작 거리가 1이여서 1을 빼줘야 함)

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    que = deque()
    que.append((x, y))
    
    while que:
        x, y = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
            elif graph[nx][ny] > graph[x][y] + 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))

    return

n, m = map(int, input().split())
graph = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
cnt = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

print(max(map(max, graph))-1)