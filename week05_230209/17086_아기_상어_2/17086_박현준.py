from collections import deque
def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    dx = [-1, -1, -1, 0, 1, 0, 1, 1]
    dy = [-1, 0, 1, 1, 1, -1, 0, -1]
    while queue:
        x, y, distance = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if lst[nx][ny] == 0:
                    queue.append((nx, ny, distance+1))
                    visited[nx][ny] = True
                else:
                    return distance + 1

n, m = map(int, input().split())
lst = [[int(x) for x in input().split()] for _ in range(n)]
res = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            res = max(res, bfs(i, j))
print(res)