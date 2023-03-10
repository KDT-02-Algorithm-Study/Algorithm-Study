# 16974 레벨 햄버거

def bur(n, x):
    # 종료 조건
    if n == 0:
        if x == 0:
            return 0
        else:
            return 1
        
    b = 2**(n+2)-3  # 현재 단계 버거크기
    bb = 2**(n+1)-3 # 이전 단계 버거크기

    p = 2**(n+1)-1  # 현재 단계 패티 개수
    pp = 2**n-1     # 이전 단계 패티 개수
    
    # 분할
    if x == 1:          # 왼쪽 끝
        return 0
    elif bb+2 > x:      # 왼쪽
        return bur(n-1, x-1)
    elif bb+2 == x:     # 중앙
        return pp + 1
    elif bb+2 < x < b:  # 오른쪽
        # 왼쪽은 먹었다고 생각하고 길이는 bb+2(이전단계+첫번째빵+중앙패티)만큼 마이너스 # 패티는 pp+1(이전단계+중앙패티)만큼 플러스
        return pp + 1 + bur(n-1, x-bb-2) 
    else:               # 오른쪽 끝 # b == x
        return p

# X는 먹어야할 버거(빵+패티)의 길이
N, X = map(int, input().split())
print(bur(N, X))


""" 
0
-010-
--010-2-010--
---010-2-010--3--010-2-010---
----010-2-010--3--010-2-010---4---010-2-010--3--010-2-010----
"""

'''
N = 3 일 때
- - - p p p - p - p p p - - p - - p p p - p - p p p - - - 
1 2 3 4 5 6 7 8 9 1011121314151617181920212223242526272829
'''