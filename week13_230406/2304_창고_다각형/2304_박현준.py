# 31256 KB / 108 ms

N = int(input())
lst = []
index = 0
max_height = 0
max_height_index = 0
total = 0

# 리스트에 담기
for _ in range(N):
    L, H = map(int, input().split())
    lst.append((L, H))
lst = sorted(lst)

# 최대값 찾기
for i in lst:
    if max_height < i[1]:
        max_height = i[1]
        max_height_index = index
    index += 1

cur = lst[0][1]

for i in range(max_height_index):
    if cur < lst[i+1][1]:
        tmp = cur * (lst[i+1][0] - lst[i][0])
        total += tmp
        cur = lst[i+1][1]
    else:
        total += cur * (lst[i+1][0] - lst[i][0])

cur = lst[-1][1]

for i in range(N-1, max_height_index, -1):
    if cur < lst[i-1][1]:
        total += cur * (lst[i][0] - lst[i-1][0])
        cur = lst[i-1][1]
    else:
        total += cur * (lst[i][0] - lst[i-1][0])

print(total + max_height)