# 34308 KB / 76 ms

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d, C):
    if C == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
snake = deque([(0,0)])
x, y = 0, 0
d = 0
board[0][0] = 1
direction = {}
time = 0
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 2
L = int(input())
for _ in range(L):
    X, C = input().split()
    direction[int(X)] = C

while True:
    time += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if nx >= N or nx < 0 or ny >= N or ny < 0:
        break
    if board[nx][ny] == 2:
        board[nx][ny] = 1
        snake.append((nx, ny))
    elif board[nx][ny] == 0:
        board[nx][ny] = 1
        snake.append((nx, ny))
        x, y = snake.popleft()
        board[x][y] = 0
    else:
        break
    if time in direction.keys():
        d = turn(d, direction[time])
    x = nx
    y = ny
print(time)