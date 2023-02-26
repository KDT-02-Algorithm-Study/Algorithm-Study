# 10448 유레카 이론

import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline

d = [i*(i+1)//2 for i in range(1, 47)] # 삼각수 데이터
c = list(cwr(d, 3)) # 삼각수의 중복조합 데이터

m = int(input()) # 테스트 케이스
for _ in range(m): 
    n = int(input()) # target number
    for j in c: # 중복조합 데이터 탐색
        if sum(j) == n:
            print(1)
            break
    else: # for else
        print(0)