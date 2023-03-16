# 65512 KB / 476 ms

C, R = map(int, input().split())
K = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = [[0] * C for _ in range(R)]
graph[0][0] = 1
x = 0
y = 0
dir = 0

is_exit = False

if K > C * R:
    print(0)
    is_exit = True

if not is_exit:
    for i in range(2, K+1):
        while True:            
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == 0:
                graph[nx][ny] = i
                x = nx
                y = ny
                break
            else:
                dir = (dir + 1) % 4
    print(y+1, x+1)