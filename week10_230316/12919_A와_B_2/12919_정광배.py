# 12919 A와 B 2
# 34128 KB / 68 ms

from collections import deque

# bfs
def f(t):
    q = deque()
    q.append(t)
    v.add(t)
    while q:
        t = q.popleft()
        # 일치하면 True
        if t == s:
            return True
        # 길이가 같은데 다른경우 다음 deque 탐색
        if len(t) == L:
            continue

        if t[-1] == 'A':
            A = t[:-1]
            if A not in v:
                q.append(A)
                v.add(A)

        if t[0] == 'B':
            B = t[:0:-1]
            if B not in v:
                q.append(B)
                v.add(B)
    return False
    
s = input()
t = input()

L = len(s)
v = set() # visited

# T부터 길이를 줄여가며 탐색
if f(t):
    print(1)
else:
    print(0)