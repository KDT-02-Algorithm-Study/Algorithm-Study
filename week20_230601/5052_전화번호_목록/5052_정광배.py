# 5052 전화번호 목록
# 33300 KB / 380 ms

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    data = {input().rstrip() for _ in range(n)}
    
    nums = list(data)
    f = 0
    # 모든 숫자 확인
    for num in nums:
        for j in range(len(num)): 
            if num[:j] in data: # 부분 문자열이 data에 있는지 확인
                f = 1
                break
        if f:
            break
    if f:
        print('NO')
    else:
        print('YES')