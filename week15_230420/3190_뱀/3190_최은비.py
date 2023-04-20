# 뱀 https://www.acmicpc.net/problem/3190
# 34184KB / 68ms

import sys
from collections import deque
input = sys.stdin.readline

# 우 상 좌 하
dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
idx = 0
# 뱀 출발점은 (0, 0)
snake = deque([(0, 0)])
time = 0

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())

for _ in range(k):
    i, j = map(int, input().split())
    # 사과가 있는 곳
    board[i-1][j-1] = 1

l = int(input())
# 방향 변환 정보를 담을 리스트
oper = [0] * 10001

for _ in range(l):
    # L 왼쪽 D 오른쪽
    t, d = input().split()
    oper[int(t)] = d

while True:
    dx, dy = snake.pop()
    snake.append((dx, dy))
    nx = dx + dxy[idx][0]
    ny = dy + dxy[idx][1]

    time += 1

    # 보드 범위를 벗어나거나 몸통에 닿으면 게임 종료
    if 0 > nx or nx >= n or 0 > ny or ny >= n or (nx, ny) in snake:
        break
    
    snake.append((nx, ny))

    # 사과가 없는 칸이면 꼬리 자르기
    if board[nx][ny] == 0:
        snake.popleft()
    else:
        # 사과가 있는 칸이면 꼬리는 냅두고 사과만 먹기
        board[nx][ny] = 0

    # 방향을 전환해야할 시간이면 전환하기
    if oper[time] == 'D':
        idx = (idx - 1) % 4
    elif oper[time] == 'L':
        idx = (idx + 1) % 4

print(time)