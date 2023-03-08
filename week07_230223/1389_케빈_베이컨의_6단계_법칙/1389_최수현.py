import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b):
    q = deque([(a, 0)])
    check[a] = True

    while q:
        x, cnt = q.popleft()
        if x == b:
            f_cnt[a] += cnt
            f_cnt[b] += cnt
            return
        
        for f in friends[x]:
            if not check[f]:
                check[f] = True
                q.append((f, cnt+1))

n, m = map(int, input().split())
friends = [[] for _ in range(n)]
f_cnt = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

for i in range(n-1):
    for j in range(i+1, n):
        check = [False] * (n)
        bfs(i, j)

print(f_cnt.index(min(f_cnt))+1)