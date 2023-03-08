# 11497 통나무 건너뛰기
# 32276 KB / 188 ms

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    
    # 정렬
    l = sorted(L)

    # 홀수번째 짝수번째 나눴는데 필요없는것 같다
    c1 = c2 = 0
    for i in range(n-2):
        if i & 1:
            c11 = l[i+2]-l[i]
            if c11 > c1:
                c1 = c11
            # max가 더 느림
            # c1 = max(c1, l[i+2]-l[i])
        else:
            c22 = l[i+2]-l[i]
            if c22 > c2:
                c2 = c22
            # c2 = max(c2, l[i+2]-l[i])
    print(max(c1, c2))