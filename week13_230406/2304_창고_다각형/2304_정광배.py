# 2304 창고 다각형
# 31256 KB / 40 ms

import sys
input = sys.stdin.readline

n = int(input()) # 막대 개 수
g = [0]*1001
long_ = 0 # 가장 큰 막대의 길이
b = [] # long 막대를 저장
for _ in range(n):
    l, h = map(int, input().split())
    if h > long_: # long 이 갱신되면
        long_ = h
        a = []
    if h == long_:
        a.append(l)
    g[l] = h
    b.append(l)

# 가장 큰 막대의 양 끝 위치
long_r = max(a)
long_l = min(a) 

# 막대 양 끝 위치
p_r = max(b)
p_l = min(b)

total = 0
# long 왼쪽
d = 0
for i in range(p_l, long_l):
    if g[i] > d:
        d = g[i]
    total += d

# long 오른쪽
d = 0
for i in range(p_r, long_r, -1):
    if g[i] > d:
        d = g[i]
    total += d

# long
total += (long_r - long_l + 1)*long_

print(total)
