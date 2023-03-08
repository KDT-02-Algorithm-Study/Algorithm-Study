# 1758 알바생 강호 https://www.acmicpc.net/problem/1758
# 35892KB / 88ms
# 팁을 많이 주려는 손님을 앞으로 배치해서 받을 수 있는 팁을 최대로 만들기

import sys
input = sys.stdin.readline

n = int(input())
tip = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0

for i in range(n):
    tmp = tip[i] - i

    if tmp > 0:
        ans += tmp

print(ans)