# 19637 IF문 좀 대신 써줘
# 42036 KB / 420 ms

import sys
input = sys.stdin.readline

# 이분 탐색
def bs(lo, hi):
    # 탈출 조건
    if lo+1 >= hi: 
        return title[hi] # hi를 리턴

    mid = lo+hi >> 1 # (lo+hi)//2

    # 
    if power[mid] < now:
        return bs(mid, hi)
    else:
        return bs(lo, mid)


n, m = map(int, input().split())

power = [] # 10 10 100
title = [] # B  A  C
# data 저장
for _ in range(n):
    a, b = input().split()
    title.append(a)
    power.append(int(b))

# input 탐색
for _ in range(m):
    now = int(input())
    print(bs(-1,n-1)) # binary_search

'''
1 10 10 100 : power
A B  C  D   : title

now = 9
power[mid] < now
1 0 0 0
  ↑
  
now = 10
power[mid] < now
1 0 0 0
  ↑
  
now = 11
power[mid] < now
1 1 1 0
      ↑

now = 100
power[mid] < now
1 1 1 1
      ↑ n-1
'''