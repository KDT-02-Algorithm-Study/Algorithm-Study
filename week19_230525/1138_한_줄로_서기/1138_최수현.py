# 31256 KB / 44 ms

import sys
input = sys.stdin.readline

n = int(input())
rank = list(map(int, input().split()))
line = [0] * n

for i in range(n):
    cnt = 0
    # 0의 개수를 세면서 개수가 맞는 지점에 값 입력
    for j in range(n):
        if line[j] == 0:
            if cnt == rank[i]:
                line[j] = i + 1
                break
            else:
                cnt += 1
print(*line)