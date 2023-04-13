# 2469 사다리 타기
# 31256 KB / 44 ms

import sys
input = sys.stdin.readline

k = int(input().rstrip()) # 사람 수
n = int(input().rstrip()) # 사다리 길이
start = list(range(k)) # 시작 순서 [1, 2, 3, ...]
# 최종 순서를 아스키코드로 받음 
end = [ord(x)-65 for x in list(input().rstrip())] 

# 첫줄부터 ?줄까지 start 변경
for m in range(n):
    line = input().rstrip()
    # ?를 만나면 탈출
    if line == '?'*(k-1):
        break
    # '-'를 만나면 i와 i+1 스왑
    for i in range(k-1):
        if line[i] == '-':
            start[i], start[i+1] = start[i+1], start[i]

# ?줄부터 끝까지 d에 담기
d = []
for _ in range(n-m-1):
    d.append(input().rstrip())

# 끝줄부터 ?줄까지 end 변경
for line in d[::-1]:
    for i in range(k-1):
        # '-'를 만나면 스왑
        if line[i] == '-':
            end[i], end[i+1] = end[i+1], end[i]

# 변경된 start와 end를 비교하며 사다리 놓기
result = ''
for i in range(k-1):
    # 같을 경우 '*' 추가
    if start[i] == end[i]:
        result += '*'
    # 바꿔야 하는 경우 '-' 추가
    elif start[i] == end[i+1]:
        result += '-'
        start[i], start[i+1] = start[i+1], start[i]
    # 성립이 안될 때
    else:
        result = 'x'*(k-1)
        break

print(result)