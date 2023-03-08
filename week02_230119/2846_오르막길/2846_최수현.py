import sys

n = int(input())
h = list(map(int, sys.stdin.readline().split()))
cnt = 0
hill = []

for i in range(n-1):
    if h[i] < h[i+1]:
        cnt += h[i+1] - h[i]
        hill.append(cnt)
    else:
        cnt = 0

print(max(hill) if hill else 0)