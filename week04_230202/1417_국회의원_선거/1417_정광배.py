# 1417 국회의원 선거

import sys
input = sys.stdin.readline

n = int(input())
d = int(input())
c = [int(input()) for _ in range(n-1)]
cnt = 0
if n == 1:
    print(0)
else:
    while d <= max(c): # 최댓값이 d보다 작을 때까지
        c[c.index(max(c))] -= 1 # 최댓값에서 하나씩 빼서
        d += 1          # d에 추가
        cnt += 1
    print(cnt)