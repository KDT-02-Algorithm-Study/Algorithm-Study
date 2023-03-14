import sys
input = sys.stdin.readline

def dfs(b, a, rain):
    stack = [(b, a)]
    check[b][a] = True

    while stack:
        y, x = stack.pop()
        for dy, dx in delta:
            yy = y + dy
            xx = x + dx
            if 0 <= yy < n and 0 <= xx < n:
                if region[yy][xx] > rain and not check[yy][xx]:
                    stack.append((yy, xx))
                    check[yy][xx] = True

n = int(input())
region = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
safe_zone = 1
min_ = min([min(region[i]) for i in range(n)])
max_ = max([max(region[i]) for i in range(n)])

for r in range(min_, max_):
    check = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if region[i][j] > r and not check[i][j]:
                dfs(i, j, r)
                cnt += 1
    
    if cnt > safe_zone:
        safe_zone = cnt

print(safe_zone)