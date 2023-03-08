dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, apple):
    visited[x][y] = True
    global res
    if cnt > 3:
        return
    if apple > 2:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and graph[nx][ny] != -1:
            visited[nx][ny] = True
            if graph[nx][ny] == 1:
                dfs(nx, ny, cnt + 1, apple + 1)
            else:
                dfs(nx, ny, cnt+1, apple)
            visited[nx][ny] = False
    if res < apple:
        res = apple

graph = [[int(x) for x in input().split()] for _ in range(5)]
visited = [[False for _ in range(5)] for _ in range(5)]
r, c = map(int, input().split())

res = 0
dfs(r, c, 0, 0)
if res >= 2:
    print(1)
else:
    print(0)