# 31256 KB / 44ms
import sys
S=list(input())
T=list(input())
def dfs(T):
    if T==S:
        print(1)
        sys.exit()
    if len(S) > len(T):
        return False
    if T[-1]=='A':
        dfs(T[:-1])
    if T[0]=='B':
        T = T[1:]
        dfs(T[::-1])
dfs(T)
print(0)