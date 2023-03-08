import sys
input = sys.stdin.readline
from collections import deque

def bfs(q):
    day = 0

    while q:
        y, x, d = q.popleft()
        day = d
        for dy, dx in delta:
            yy = y + dy
            xx = x + dx
            if 0 <= yy < n and 0 <= xx < m:
                if not check[yy][xx]:
                    check[yy][xx] = True
                    q.append((yy, xx, d+1))
    return day

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j, 0))
            check[i][j] = True
        elif tomato[i][j] == -1:
            check[i][j] = True

result = bfs(queue)
if sum([sum(check[i]) for i in range(n)]) == n * m:
    print(result)
else:
    print(-1)