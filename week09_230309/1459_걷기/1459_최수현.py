# 메모리 31256 KB, 시간 40 ms
import sys
intput = sys.stdin.readline

x, y, w, s = map(int, input().split())
x = abs(x)
y = abs(y)

if w > s:
    print(s * (min(x, y) + abs(x-y)//2*2) + w * (abs(x-y)%2))
elif w * 2 > s:
    print(s * min(x, y) + w * abs(x-y))
else:
    print(w * (x + y))