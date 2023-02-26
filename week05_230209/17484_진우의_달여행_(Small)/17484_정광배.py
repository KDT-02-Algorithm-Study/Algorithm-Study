# 17484 진우의 달여행

import sys
input = sys.stdin.readline
M = 1000

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
for s in range(m):
    g[0][s] = (g[0][s], g[0][s], g[0][s])

for i in range(1, n):
    for j in range(m):
        if j == 0:
            left_ = M
        else:
            left_ = g[i][j] + min(g[i-1][j-1][1], g[i-1][j-1][2])

        if j == m-1:
            right_ = M
        else:
            right_ = g[i][j] + min(g[i-1][j+1][0], g[i-1][j+1][1])

        up_ = g[i][j] + min(g[i-1][j][0], g[i-1][j][2])

        g[i][j] = (left_, up_, right_)

print(min(map(min,*g[n-1])))