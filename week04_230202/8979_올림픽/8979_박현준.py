N, K = map(int, input().split())
lst = [[int(x) for x in input().split()] for _ in range(N)]
lst_sort = sorted(lst, key=lambda x: (x[1], x[2], x[3]), reverse=True)
for rank in range(N):
    if lst_sort[rank][0] == K:
        res = rank
for i in range(N):
    if lst_sort[res][1:] == lst_sort[i][1:]:
        print(i + 1)
        break