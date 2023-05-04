# 2002 추월
# 31256 KB / 72 ms

import sys
input = sys.stdin.readline

n = int(input())
in_ = {}
out_ = []
for i in range(n):
    in_[input().rstrip()] = i
for _ in range(n):
    out_.append(input().rstrip())

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if in_[out_[i]] > in_[out_[j]]:
            cnt += 1
            break
print(cnt)