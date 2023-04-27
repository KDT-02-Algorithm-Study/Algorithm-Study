# 11000 강의실 배정
# 75928 KB / 340 ms

import sys
import heapq
input = sys.stdin.readline

n = int(input())
d = [tuple(map(int, input().split())) for _ in range(n)]
d = sorted(d, key=lambda x: (x[0], x[1]))
c = [d[0][1]]
for i in range(1, n):
    if d[i][0] < c[0]:
        heapq.heappush(c, d[i][1])
    else:
        heapq.heappop(c)
        heapq.heappush(c, d[i][1])
print(len(c))