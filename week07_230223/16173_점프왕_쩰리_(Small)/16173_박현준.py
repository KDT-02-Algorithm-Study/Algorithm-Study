def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    
    current = graph[x][y]
    
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x + current, y)
        dfs(x, y + current)
        return True
    return False

N = int(input())
graph = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dfs(0, 0)

if visited[N-1][N-1] == True:
    print('HaruHaru')
else:
    print('Hing')