import sys
sys.setrecursionlimit(10 ** 6)
def dfs(x, y):
    global total
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    else:
        if graph[x][y] == 1:
            total = total + 1
            graph[x][y] = 0
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True
    return False
n, m = map(int, input().split())
graph = [[int(x) for x in input().split()] for _ in range(n)]
res = total = mxm = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res += 1
            if mxm < total:
                mxm = total
            total = 0
print(res)
print(mxm)