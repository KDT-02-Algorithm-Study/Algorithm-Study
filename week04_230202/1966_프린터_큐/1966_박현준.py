from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = [int(x) for x in input().split()]
    queue = deque()
    cnt = 0
    for i, x in enumerate(lst):
        queue.append((i, x))
    lst = sorted(lst)
    while queue:
        i, x = queue.popleft()
        if x == lst[-1]:
            lst.pop()
            cnt += 1
            if i == M:
                print(cnt)
                break
        else:
            queue.append((i, x))