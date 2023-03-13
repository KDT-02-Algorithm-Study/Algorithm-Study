# 그림 https://www.acmicpc.net/problem/1926
import sys
input = sys.stdin.readline

def dfs(x, y):
    # 시작 좌표 스택에 삽입하고 방문처리
    # 여기서 방문처리는 1을 0으로 바꿔서 다시 탐색하지 않도록 하는 것을 의미
    stack = [(x, y)]
    paper[x][y] = 0
    cnt = 0

    while stack:
        # 연결된 부분으로 옮겨갈 때마다 cnt+1
        cnt += 1
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위에서 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 빈 도화지면 무시
            if paper[nx][ny] == 0:
                continue
            if paper[nx][ny] == 1:
                paper[nx][ny] = 0
                stack.append((nx, ny))
    
    return cnt


n, m = map(int, input().split())
paper = []
# 가로세로 탐색할 때 증감값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    paper.append(list(map(int, input().split())))

res = []

for i in range(n):
    for j in range(m):
        # 그림 시작하는 부분 찾아서 bfs 진행
        if paper[i][j] == 1:
           res.append(dfs(i, j))

if res:
    print(len(res), max(res), sep="\n")
else:
    print(0, 0, sep="\n")