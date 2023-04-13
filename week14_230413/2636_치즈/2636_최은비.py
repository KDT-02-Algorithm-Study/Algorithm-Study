# 치즈 https://www.acmicpc.net/problem/2636
# 34168KB / 84ms
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    que = deque()
    que.append((0, 0))
    visited[0][0] = True
    cnt = 0 # 한시간 동안 녹인 치즈 갯수

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    que.append((nx, ny))
                elif graph[nx][ny] == 1:
                    # 외부 공기에 접촉된 치즈 녹이기
                    # 1일 때도 큐에 담으면 공기에 접촉되지 않은 구멍을 둘러싼 치즈도 녹여버리기 때문에 큐에 담지 않고 갯수만 더해줌
                    graph[nx][ny] = 0
                    cnt += 1

    return cnt


r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = [] # 시간별로 녹인 치즈 갯수를 기록하는 리스트
time = 0

while True:
    visited = [[False] * c for _ in range(r)]
    cnt = bfs()

    # 이번 시간 동안 녹인 치즈가 없으면 반복문 탈출
    if cnt == 0:
        break
    
    time += 1
    ans.append(cnt)

print(time)
print(ans[-1])

