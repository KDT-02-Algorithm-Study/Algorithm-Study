# 2578 빙고

import sys
input = sys.stdin.readline

a, b = [], []
for k in range(10):
    if k < 5:
        a += list(input().split())
    else:
        b += list(input().split())

cnt = 0       
for i in range(25):
    idx = a.index(b[i])
    a[idx] = 0

    if all(a[ny] == 0 for ny in range(25) if ny % 5 == idx % 5):
        cnt += 1
    if all(a[nx] == 0 for nx in range(25) if nx // 5 == idx // 5):
        cnt += 1
    if idx % 6 == 0 and all(a[n1] == 0 for n1 in range(25) if n1 % 6 == 0):
        cnt += 1
    if idx in range(4, 24, 4) and all(a[n1] == 0 for n1 in range(4, 24, 4)):
        cnt += 1

    if cnt >= 3:
        break

print(i+1)

'''
0  1  2  3  4
5  6  7  8  9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
'''