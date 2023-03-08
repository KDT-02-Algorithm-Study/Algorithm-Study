# 16953 A → B
# 36628 KB / 132 ms

from collections import deque

# bfs
def bfs(x):
    c = 0
    q = deque([(x, c)])
    d.add(x)
    while q:
        x, c = q.popleft()
        c+=1
        if x == b:
            return c 
        t1 = x*2
        t2 = int(str(x)+'1')
        if t1 <= b:
            if t1 not in d:
                q.append((t1, c))
                d.add(t1)
        if t2 <= b:
            if t2 not in d:
                q.append((t2, c))
                d.add(t2)
    return -1


a, b = map(int, input().split())
d = set()
print(bfs(a))