# 31364 KB / 44 ms

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = input().rstrip()
l = len(s)
T = input().rstrip()
res = []

def plus(t):
    if len(t) == l:
        if t == s:
            res.append(1)
        return
    if t[-1] == 'A':
        plus(t[:-1])
    elif t[-1] == 'B':
        plus(t[-2::-1])

plus(T)
print(1 if res else 0)