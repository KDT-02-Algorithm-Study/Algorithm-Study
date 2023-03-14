import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    farm[y][x] = 0
    for dx, dy in delta:
        move_x = x + dx
        move_y = y + dy
        if 0 <= move_x < m and 0 <= move_y < n and farm[move_y][move_x]:
            dfs(move_y, move_x)
    return

delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        farm[b][a] = 1

    cnt = 0
    for b in range(n):
        for a in range(m):
            if farm[b][a]:
                dfs(b, a)
                cnt += 1
    print(cnt)