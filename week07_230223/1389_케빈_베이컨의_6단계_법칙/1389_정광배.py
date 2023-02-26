# 1389 케빈 베이컨의 6단계 법칙
# 34176KB 60ms 606B

import sys
sys.stdin = open('input_1389.txt', 'r')

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, d):
    global c
    q = deque()
    q.append((x, d))
    v[x] = 1
    while q:
        x, d = q.popleft()
        c += d
        d += 1
        for e in g[x]:
            if not v[e]:
                q.append((e, d))
                v[e] = 1

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

t = 1e9
for i in range(1, n+1):
    v = [0] * (n+1)
    c = 0
    bfs(i,0)
    if c < t:
       r = i
       t = c 
print(r)