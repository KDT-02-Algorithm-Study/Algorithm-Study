N, K = map(int, input().split())
lst = [x for x in range(1, N+1)]
res = []
loop = 0
for i in range(N):
    loop = (loop + (K - 1)) % len(lst)
    res.append(lst.pop(loop))
print('<' + ', '.join(map(str, res)) + '>')