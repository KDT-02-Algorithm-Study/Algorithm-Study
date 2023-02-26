# 1780 종이의 개수

import sys
input = sys.stdin.readline

n = int(input())
s = n
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = [0, 0, 0]

while s > 0:
    for i in range(0,n,s):
        for j in range(0,n,s):
            key = graph[i][j]
            if key == 2:
                continue
            for x in range(0, s):
                for y in range(0, s):
                    if graph[i+x][j+y] != key:
                        break
                if graph[i+x][j+y] != key:
                    break
            else:
                cnt[key+1] += 1
                for x in range(0, s):
                    for y in range(0, s):
                        graph[i+x][j+y] = 2
    s //= 3
print(*cnt, sep='\n')