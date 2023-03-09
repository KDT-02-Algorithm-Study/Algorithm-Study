# 35892 KB / 96 ms

import sys
N = int(input())
tips = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)], reverse=True)
total = 0

# 받을 팁이 양수면 total에 더해준다
for index, tip in enumerate(tips):
    tip_take = tip - (index + 1 - 1)
    if tip_take > 0:
        total += tip_take
print(total)