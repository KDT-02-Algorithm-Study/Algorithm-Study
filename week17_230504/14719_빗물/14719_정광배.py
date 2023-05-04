# 14719 빗물
# 31256 KB / 44 ms

h, w = map(int, input().split()) # 높이 길이
d = list(map(int, input().split())) # 3 1 2 3 4 1 1 2

total = 0
stack = [] # 블록 인덱스가 담길 stack

# 블럭 탐색(인덱스)
for i in range(w):
    now = d[i]
    # 현재 높이가 이전 높이보다 크다면
    while stack and now > d[stack[-1]]:
        low = stack.pop()
        if not stack:
            break
        gap = min(now, d[stack[-1]]) - d[low] # 높이 차이
        width = i-stack[-1] - 1 # 길이
        total += (width * gap)
    stack.append(i)
print(total)

'''
0
0 1
0 2
0 3
4
4 5
4 5 6
4 7
'''