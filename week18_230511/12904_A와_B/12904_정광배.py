# 12904 A와 B
# 31388 KB / 40 ms

import sys
sys.setrecursionlimit(int(1e6))

# 재귀
def f(t):
    # 일치하면 True
    if t == s:
        return True
    # 길이가 같은데 다른경우 False
    if len(t) == L:
        return False
    # 끝이 B일 때
    if t[-1] == 'B':
        return f(t[:-1][::-1])
    # 끝이 A일 때
    else:
        return f(t[:-1])

s = input()
t = input()

L = len(s)
if f(t):
    print(1)
else:
    print(0)