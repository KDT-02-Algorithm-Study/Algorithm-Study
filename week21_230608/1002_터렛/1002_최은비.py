# 터렛 https://www.acmicpc.net/problem/1002
# 31256KB / 40ms
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = (x1 - x2)**2 + (y1 - y2)**2

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (r1 + r2)**2 < dis:
            print(0)
        elif (r1 + r2)**2 == dis:
            print(1)
        elif (r1 - r2)**2 == dis:
            print(1)
        elif (r1 - r2)**2 > dis:
            print(0)
        else:
            print(2)