# 2503 숫자 야구
# 31256 KB / 44 ms

import sys
from itertools import permutations
input = sys.stdin.readline

# 모든 경우를 문자열로 리스트로 ( [('1', '2', '3'), ...])
numbers = list(permutations(map(str, range(1, 10)), 3))

n = int(input())
data = [] # 질문과 대답 저장
for _ in range(n):
    a, b, c = input().split()
    data.append((a, int(b), int(c)))

# 각각의 숫자가 질문과 대답에 일치하는지 완전 탐색
cnt = 0
for num in numbers:
    f = 0 # flag
    for e in data:
        a, s, b = e # 수, strike, ball
        for i in range(3):
            # strike 검사
            if a[i] == num[i]:
                s -= 1
                if s < 0:
                    f = 1
                    break
            # strike가 아니라면 ball검사
            elif a[i] in num:
                b -= 1
                if b < 0:
                    f = 1
                    break
        # 처리한 후 strike 와 ball의 숫자가 맞는지 검사
        if s != 0 or b != 0:
            f = 1
        if f:
            break
    # f = 1이면 다음 수 검사
    if f:
        continue
    # f = 0이면 cnt++
    cnt += 1
    
print(cnt)