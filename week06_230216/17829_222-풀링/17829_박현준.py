def pooling(lst, N):
    if N == 1:
        return lst[0][0]
    res = [[] for _ in range(int(N/2))]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            res[int(i/2)].append((sorted([lst[i][j], lst[i+1][j], lst[i][j+1], lst[i+1][j+1]])[-2]))
    return pooling(res, int(N/2))
N = int(input())
lst = [[int(x) for x in input().split()] for _ in range(N)]
print(pooling(lst, N))