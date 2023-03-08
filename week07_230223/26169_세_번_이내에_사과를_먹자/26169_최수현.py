import sys
input = sys.stdin.readline

def dfs(y, x, moving, apple):
    global result
    check[y][x] = True
    apple += board[y][x]

    if moving == 3:
        if apple >= 2:
            result = 1
            return
        else:
            return

    for dy, dx in delta:
        yy = y+dy
        xx = x+dx
        if 0 <= yy < 5 and 0 <= xx < 5:
            if board[yy][xx] != -1 and not check[yy][xx]:
                dfs(yy, xx, moving+1, apple)
                check[yy][xx] = False

board = [list(map(int, input().split())) for _ in range(5)]
check = [[False]*5 for _ in range(5)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0

r, c = map(int, input().split())
dfs(r, c, 0, 0)
print(result)