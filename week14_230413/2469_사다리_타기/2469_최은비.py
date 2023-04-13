# 사다리 타기 https://www.acmicpc.net/problem/2469
# 31256KB / 44ms
# ?? 전까지 사다리를 타고 내려온 결과와 입력으로 들어온 결과에서 ?? 전까지 사다리를 타고 올라간 결과를 각각 저장

import sys
input = sys.stdin.readline

k = int(input()) # 사람 수
n = int(input()) # 놓아야 하는 가로 줄 수
end = list(input().strip())
start = sorted(end)
ladder = [list(input().strip()) for _ in range(n)]
top = [] # ?? 위의 사다리 모양을 저장
bottom = [] # ?? 아래의 사다리 모양을 저쟝

for i in range(n):
    if ladder[i] == ["?" for _ in range(k-1)]:
        top = bottom
        bottom = []
        continue
    
    bottom.append(ladder[i])

# 위에서 아래로 내려가야 하니까 첫번째 사다리 모양부터 꺼내서 비교
while top:
    tmp = top.pop(0)

    for i in range(k-1):
        if tmp[i] == '-':
            start[i], start[i+1] = start[i+1], start[i]

# 아래에서 위로 올라와야 하니까 마지막 사다리 모양부터 꺼내서 비교
while bottom:
    tmp = bottom.pop()

    for i in range(k-1):
        if tmp[i] == '-':
            end[i], end[i+1] = end[i+1], end[i]

# 위에서 저장한 두 리스트를 비교해서 사다리 모양을 만들기
ans = ['*' for _ in range(k-1)]
for i in range(k-1):
    if start[i] == end[i+1] and start[i+1] == end[i]:
        ans[i] = '-'
        start[i], start[i+1] = start[i+1], start[i]

if start == end:
    print(*ans, sep='')
else:
    print('x'*(k-1))