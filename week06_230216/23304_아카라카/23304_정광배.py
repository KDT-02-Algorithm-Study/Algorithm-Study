# 23304 아카라카

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def a(s):
    # 종료 조건
    if len(s) == 1:
        return True
    
    l = len(s)//2

    if s[:l] != s[-l:]:
        return False
    
    # 재귀
    return a(s[:l])

S=input().rstrip()

if a(S):
    print('AKARAKA')
else:
    print('IPSELENTI')