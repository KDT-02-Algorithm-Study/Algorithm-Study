import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    floor = list(range(1, n+1))
    for j in range(k):
        next_floor = []
        for l in range(n):
            if l == 0:
                next_floor.append(1)
            else:
                next_floor.append(next_floor[-1]+floor[l])
        floor = next_floor
    print(floor[-1])