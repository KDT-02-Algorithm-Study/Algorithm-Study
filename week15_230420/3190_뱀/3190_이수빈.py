# 3190 뱀
# 34176 KB / 68ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
Dict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = input().split()
    Dict[int(x)] = c


x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(d):
    global direction
    if d == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]


    # 벽에 부닥침ㄴ 끝
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    
    # 몸통 늘리기 
    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in Dict:
            turn(Dict[cnt])
    
    # 몸통이 짤ㅂ아짐
    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        nx, ny = queue.popleft()
        graph[nx][ny] = 0
        if cnt in Dict:
            turn(Dict[cnt])
    # 1 만나면 끝나는거
    else :
        break
print(cnt)





    




