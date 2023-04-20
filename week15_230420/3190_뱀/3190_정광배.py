# 3190 뱀
# 34192 KB / 68 ms

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 보드 크기
K = int(input()) # 사과의 개수
apple = set(tuple(map(int, input().split())) for _ in range(K)) # 사과 위치
L = int(input()) # 방향 변환 횟수
d = [] # 방향 변환을 담을 리스트 (X, D)
for _ in range(L):
    X, D = input().split()
    X = int(X)
    d.append((X, D))

# 우 하 좌 상
di = ((0, 1), (1, 0), (0, -1), (-1, 0))
head = 0 # 진행 방향 # 처음은 오른쪽

snake = deque([(1, 1)]) # 뱀이 차지하는 칸
x = y = 1 # 머리 위치
t = 0 # 시간
a = 0 # 방향 변환 인덱스(d 전용 인덱스) a < L

# 탈출할 때까지 반복
while True:
    t += 1 # 시간 증가

    # head방향으로 진행
    nx = x + di[head][0]
    ny = y + di[head][1]
    # 벽에 부딪힐 때 
    if nx <= 0 or nx > N or ny <= 0 or ny > N:
        break
    # 몸에 부딪힐 때
    if (nx, ny) in snake:
        break

    # 진행가능 할 때
    snake.append((nx, ny)) # 몸 늘어남

    if (nx, ny) in apple: # 사과 만났을 때
        apple.remove((nx, ny)) # 사과 먹고 사과 제거
    else: # 사과가 아닐 때
        snake.popleft() # 몸 짧아짐
    
    # 방향 회전
    if a < L:
        if t == d[a][0]: # 현재 시간이 회전 시간[a][0]과 일치 할 경우
            if d[a][1] == 'L': # 좌회전
                head = (head+3)%4
            else: # 우회전
                head = (head+1)%4
            a += 1
    x, y = nx, ny # 머리 갱신
print(t) # 시간 출력