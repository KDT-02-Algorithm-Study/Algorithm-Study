# 31388 KB / 416 ms

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]


N, M = map(int, input().split())
lst = [[int(x) for x in input().split()] for _ in range(N)]

op = [[int(x) for x in input().split()] for _ in range(M)]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for i in range(M):
    x, y = op[i]
    x -= 1
    next = []
    for j in clouds:
        nx = (j[0] + dx[x] * y ) % N
        ny = (j[1] + dy[x] * y ) % N
        next.append([nx, ny])
    visited = [[False] * N for _ in range(N)]
    for j in next:
        a = j[0]
        b = j[1]
        lst[a][b] += 1
        visited[a][b] = True
    clouds = []
    
    for X, Y in next:
        cnt = 0
        for i in range(4):
            nX = X + dx2[i]
            nY = Y + dy2[i]
            if -1 < nX < N and -1 < nY < N and lst[nX][nY]:
                cnt += 1
        lst[X][Y] += cnt
    
    for i in range(N):
        for j in range(N):
            if lst[i][j] >= 2 and not visited[i][j]:
                lst[i][j] -= 2
                clouds.append([i, j])
res = 0
for i in range(N):
    res += sum(lst[i])
print(res)