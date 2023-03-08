from collections import deque

n, k = map(int, input().split())
nums = deque(range(1, n+1))
yo = deque()
while len(yo) < n:
    for _ in range(k-1):
        nums.append(nums.popleft())
    yo.append(nums.popleft())

print('<', end='')
print(*yo, sep=', ', end='>')