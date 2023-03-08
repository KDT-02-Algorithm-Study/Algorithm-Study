# 1758 알바생 강호
# 35892 KB / 92 ms

import sys
input = sys.stdin.readline

n = int(input())

tips = [int(input()) for _ in range(n)]
tips = sorted(tips, reverse=True)
cnt = 0
# 팁이 많은 순서부터 받고 loop마다 팁 -1씩 누적
for i in range(n):
    if tips[i]-i > 0:
        cnt += tips[i]-i
    else:
        break
print(cnt)