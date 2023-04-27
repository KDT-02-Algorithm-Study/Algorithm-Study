# 1406 에디터
# 41676 KB / 324 ms

import sys
input = sys.stdin.readline

s = list(input().rstrip())
m = int(input())
r = []
for _ in range(m):
    a, *b = input().split()
    if a == 'L':
        if s:
            r.append(s.pop())
    elif a == 'D':
        if r:
            s.append(r.pop())
    elif a == 'B':
        if s:
            s.pop()
    else:
        s.append(b[0])
print(''.join(s+r[::-1]))
