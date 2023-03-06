# https://www.acmicpc.net/submit/2309/54323905
# 9개의 수 중에 7개의 합이 100
# 9개를 모두 더한 값에서 100을 뺀 값과 두 수를 더했을 때 값이 같으면 그 두 수를 뺀 7개를 출력

import sys

input = sys.stdin.readline

height = [0 for i in range(9)]

for i in range(9):
    height[i] = int(input())

height = sorted(height)
gap = sum(height) - 100
fake1 = 0
fake2 = 0

for i in range(8):
    for j in range(i+1, 9):
        if height[i] + height[j] == gap:
            fake1 = height[i]
            fake2 = height[j]
            break

for ans in height:
    if ans == fake1:
        continue
    elif ans == fake2:
        continue
    else:
        print(ans)
