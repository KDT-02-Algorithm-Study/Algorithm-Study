# 
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
trace = [[False] * n for _ in range(n)]
apple = [[0] * n for _ in range(n)]
        #  우      하       좌       상
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
      # y  x  d
head = [0, 0, 0]
tail = [0, 0, 0]

for _ in range(int(input())):
    i, j = map(int, input().split())
    apple[i-1][j-1] = 1

# 회전 시점
head_turn = deque()
for _ in range(int(input())):
    t, c = input().split()
    t = int(t)
    head_turn.append((t, c))

# 꼬리가 회전해야하는 좌표와 방향 저장
tail_turn = deque()
trace[0][0] = True
sec = 0
while 1:
    ny = head[0] + delta[head[2]][0]
    nx = head[1] + delta[head[2]][1]
    sec += 1

    if ny < 0 or ny >= n or nx < 0 or nx >= n or trace[ny][nx]:
        break
    
    # 머리 이동
    trace[ny][nx] = True
    head[0] = ny
    head[1] = nx
    if apple[ny][nx]:
        apple[ny][nx] = 0
    # 사과 없으면 꼬리 이동
    else:
        trace[tail[0]][tail[1]] = False
        tail[0] += delta[tail[2]][0]
        tail[1] += delta[tail[2]][1]

    # 머리 회전
    if head_turn and sec == head_turn[0][0]:
        t, c = head_turn.popleft()
        if c == 'L':
            head[2] = (head[2] + 3) % 4
        else:
            head[2] = (head[2] + 1) % 4
        tail_turn.append((head[0], head[1], c))
    
    # 꼬리 회전
    if tail_turn and tail[0] == tail_turn[0][0] and tail[1] == tail_turn[0][1]:
        x = tail_turn.popleft()
        if x[2] == 'L':
            tail[2] = (tail[2] + 3) % 4
        else:
            tail[2] = (tail[2] + 1) % 4

print(sec)