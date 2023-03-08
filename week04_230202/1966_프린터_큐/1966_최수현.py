import sys
from collections import deque

t = int(input())
for _ in range(t):
    n, index = map(int, input().split())
    q = deque(map(int, sys.stdin.readline().split()))
    cnt = 0

    while 1:
        big_n = max(q)
        if q[0] == big_n:
            cnt += 1
            if index == 0:
                break
            else:
                q.popleft()
                index -= 1
        else:
            q.append(q.popleft())
            index = len(q)-1 if index == 0 else index-1
    print(cnt)