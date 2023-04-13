# 2636 치즈
# 34168 KB / 80 ms

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    cnt = 0
    q = deque([(0,0)])
    v[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx >= n or ny >= m or nx < 0 or ny < 0 or v[nx][ny]:
                continue
            if g[nx][ny] == '0':
                q.append((nx, ny))
            else: # 치즈일 경우 다음 탐색을 위해 '0'으로 바꾸고 cnt++
                g[nx][ny] = '0'
                cnt += 1
            v[nx][ny] = 1 # 방문 처리
    if cnt: # 치즈가 남아있었던 경우
        result[0] = cnt
        return False
    else: # 치즈가 다 녹았을 때
        return True

# 우 하 좌 상
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
g = [input().split() for _ in range(n)]

time = 0
result = [0]
# 치즈가 다 녹을 때 까지 탐색 반복
while True:
    v = [[False]*m for _ in range(n)]
    if bfs():
        break
    time += 1

print(time, result[0], sep='\n')