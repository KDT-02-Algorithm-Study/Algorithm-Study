from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs():
    global cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

M, N = map(int, input().split())
graph = [[int(x) for x in input().split()] for _ in range(N)]
queue = deque(())
cnt = 0
mxm = 0
stop = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
dfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            stop = 1
            break
    if stop:
        break
else:
    for i in graph:
        if mxm < max(i):
            mxm = max(i)
    print(mxm-1)