import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def bfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] > height and visited[x][y] == False:
        visited[x][y] = True
        bfs(x+1, y)
        bfs(x-1, y)
        bfs(x, y+1)
        bfs(x, y-1)
        return True
    return False

N = int(input())
graph = []
height,  max_height,  safe_area,  max_safe_area = 0, 0, 0, 0

for _ in range(N):
    lst = list(map(int, input().split()))
    if max_height < max(lst):
        max_height = max(lst)
    graph.append(lst)

while height < max_height:
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if bfs(i, j) == True:
                safe_area += 1
    if max_safe_area < safe_area:
        max_safe_area = safe_area
    safe_area = 0
    height += 1
        
print(max_safe_area)