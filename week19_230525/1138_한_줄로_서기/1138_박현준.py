# 31256 KB / 40 ms

N = int(input())
lst = [int(x) for x in input().split()]
res = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if res[j] == 0 and cnt == lst[i]:
            res[j] = i + 1
            break
        elif res[j] == 0:
            cnt += 1
print(' '.join(map(str, res)))