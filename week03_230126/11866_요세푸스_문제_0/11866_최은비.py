# https://www.acmicpc.net/problem/11866

import sys
input = sys.stdin.readline

num, cnt = map(int, input().split())
position = [i+1 for i in range(num)]
clone = position
idx = 1
res = []

while True:
    if idx % cnt == 0:
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