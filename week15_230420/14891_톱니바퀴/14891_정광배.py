# 14891 톱니바퀴
# 34176 KB / 64 ms

import sys
from collections import deque
input = sys.stdin.readline

# 회전 톱니 오른쪽 탐색
def right(a, b):
    if a == 4: # 탈출 조건 
        return
    if g[a-1][2] != g[a][6]: # 다른 극이면 
        right(a+1, b*-1) # 재귀
        g[a].rotate(b*-1) # 

# 회전 톱니 왼쪽 탐색
def left(a, b):
    if a == -1: # 탈출 조건 
        return
    if g[a+1][6] != g[a][2]: # 다른 극이면
        left(a-1, b*-1) # 재귀
        g[a].rotate(b*-1)

g = [deque(list(input().rstrip())) for _ in range(4)]
k = int(input())
# 회전
for _ in range(k):
    a, b = map(int, input().split()) # 톱니 번호, 회전 방향
    
    right(a, b) # range(a, 4)
    left(a-2, b) # reversed(range(a-1))
    g[a-1].rotate(b) # 처리후 a번째 톱니 회전

# 점수 계산
c = 1
r = 0
for i in range(4):
    r += int(g[i][0]) * c
    c *= 2
print(r)