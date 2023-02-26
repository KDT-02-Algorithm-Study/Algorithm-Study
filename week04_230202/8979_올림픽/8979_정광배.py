# 8979 올림픽

import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

h = []

for _ in range(n):
    a, g, s, b = list(map(int, input().split()))
    heapq.heappush(h, (-g, -s, -b, a))
    if a == k:
        gk, sk, bk = g, s, b # target

mg, ms, mb = [], [], []
while h:
    hp = heapq.heappop(h)
    if hp[3] == k:
        break
    if -hp[0] > gk: # 금메달 더 많은 경우
        mg.append(hp)
    elif -hp[1] > sk: # 은메달
        ms.append(hp)
    elif -hp[2] > bk: # 동메달
        mb.append(hp)

print(sum(map(len, (mg, ms, mb)))+1)