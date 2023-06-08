# 26071 오락실에 간 총총이
# 32800 KB / 2184 ms 
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
graph = [input().strip() for _ in range(n)]

minx, maxx = n, 0
miny, maxy = n, 0

for x in range(n):
    for y in range(n):
        if graph[x][y] == 'G':
            minx = min(minx,x)
            maxx = max(maxx,x)
            miny = min(miny,y)
            maxy = max(maxy,y)

res = 0 
# 최대, 최소가 같다면 한 줄에 있다는 뜻 
# 맨 끝으로 몰려면.. 가까운 벽쪽으로 몰아야함 
# 최대 -> 0 or 최소 -> n-1
# 최소값으로 구해버리기

if minx != maxx:
    res = min(n-1-minx,maxx)
if miny != maxy :
    res += min(n-1-miny,maxy)

print(res)