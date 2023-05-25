# 173212 KB / 2872 ms

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    max_n = 0
    res = 0
    # 뒤에서부터 돌면서 max_n과의 차이 res에 더하기
    for p in reversed(price):
        if p > max_n:
            max_n = p
        else:
            res += max_n - p
    print(res)