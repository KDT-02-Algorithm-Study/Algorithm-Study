# https://www.acmicpc.net/problem/13458
# 모든 응시장에 총 감독관은 무조건 1명씩 필요하므로 
# 응시생 - 총감독관이 감시할 수 있는 응시자로 부감독관이 몇명 필요한지 판별

import sys
input = sys.stdin.readline

site = int(input())
person = list(map(int, input().split()))
main, sub = map(int, input().split())
cnt = 0

for num in person:
    if num - main <= 0:
        continue
    elif num - main < sub:
        cnt += 1
    elif (num - main) % sub == 0:
        cnt += (num - main) // sub
    else:
        cnt += (num - main) // sub + 1

print(cnt + site)