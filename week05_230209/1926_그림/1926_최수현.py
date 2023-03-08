import sys

def dfs(x, y):
    stack = [(x, y)]
    check[y][x] = True
    cnt = 1

    while stack:
        cur_x, cur_y = stack.pop()
        for dx, dy in delta:
            if 0 <= cur_x+dx < m and 0 <= cur_y+dy < n:
                if paper[cur_y+dy][cur_x+dx] and not check[cur_y+dy][cur_x+dx]:
                    cnt += 1
                    check[cur_y+dy][cur_x+dx] = True
                    stack.append((cur_x+dx, cur_y+dy))
    return cnt

n, m = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
p_size = [0]
picture = 0

for y in range(n):
    for x in range(m):
        if paper[y][x] and not check[y][x]:
            p_size.append(dfs(x, y))
            picture += 1

print(picture, max(p_size), sep='\n')