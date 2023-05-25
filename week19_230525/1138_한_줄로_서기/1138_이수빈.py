# 1138 한 줄로 서기
# 31256 KB / 40 ms 
# 기본 코드


import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
ans = [0] * n

for p in range(1, n+1):
    t = h[p-1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)

