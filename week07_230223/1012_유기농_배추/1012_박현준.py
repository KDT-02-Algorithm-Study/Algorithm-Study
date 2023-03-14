import sys
sys.setrecursionlimit(10 ** 6)
def dfs(x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False
    
T = int(input())
for test_case in range(T):
    M, N, K = map(int, input().split())
    res = 0
    
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                res += 1
    print(res)