# https://www.acmicpc.net/problem/11866
# idx를 1씩 증가시키면서 k번째 사람이 되면(k로 나눴을 때 0이 되면)
# 원래 순서에서 pop한 후 결과 리스트에 append
# k번째가 아니라면 pop과 append로 맨 뒤로 보내 순서를 유지

import sys
input = sys.stdin.readline

num, k = map(int, input().split())
position = [i+1 for i in range(num)]
clone = position
idx = 1
res = []

while True:
    if idx % k == 0:
        res.append(position.pop(0))
    else:
        tmp = clone.pop(0)
        clone.append(tmp)
    
    idx += 1
    
    if len(clone) == 0:
        break

print("<", end="")
print(*res, sep=", ", end="")
print(">")