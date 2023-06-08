# 31256 KB / 40 ms
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            if r1 == 0:
                print(1)
            else:
                print(-1)
        else:
            print(0)
    else:
        distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if distance > r1 + r2 or distance < abs(r1 - r2): # 원이 안겹치는 경우
            print(0)
        elif distance == r1 + r2 or distance == abs(r1 - r2): # 원이 한 점에서 만나는 경우
            print(1)
        else: # 원이 겹치는 경우
            print(2)